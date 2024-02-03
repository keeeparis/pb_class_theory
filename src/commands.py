from asyncio import sleep
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, User
from telegram.ext import ContextTypes, ConversationHandler
from telegram.constants import ParseMode

from src.utils import *
from src.db import *

BEGIN = 100 

# helper func
def generator(x: list[Question]):
  current = 0
  
  while len(x) > current:
    yield (x[current], current)
    current += 1 
  
def process_answer(question_name: str, update: Update, context: ContextTypes.DEFAULT_TYPE):
  question: Question = context.user_data[question_name]
  
  for answer in question.answers:
    if answer.name == update.message.text:
      context.user_data['results'][answer.type] = context.user_data['results'][answer.type] + answer.value
      context.user_data['results']['total'] = context.user_data['results']['total'] + answer.value
  
  del context.user_data[question_name] 

async def calculate_result(user_data):
  values = dict([(key, value) for key, value in user_data['results'].items() if key != 'total'])
  sorted_test = dict(sorted(values.items(), key=lambda item: item[1], reverse=True))
  computed = dict([(key, int(((value / user_data['results']['total'])) * 100)) for key, value in sorted_test.items()])
  
  print(computed)

  data = []
        
  for key, value in computed.items():
    result = results[key]
    for variant in result.variants:
      if value >= variant.number:
        data.append({ 'name': result.name, 'value': value, 'type': result.type, 'description': variant.description })
        break
      
  return data
  
async def question(update: Update, context: ContextTypes.DEFAULT_TYPE, questions):
  process_answer('question', update, context)
  user = update.message.from_user
    
  try:
    (question, current) = next(questions)
    context.user_data['question'] = question
    
    await update.message.reply_text(
      question.name,
      reply_markup=create_answer_markup(question.answers),
    )

    return current
  
  except:
    await update.message.reply_text(
      "Спасибо! Вы закончили прохождение теста.",
      reply_markup=ReplyKeyboardRemove()
    )
    
    await sleep(1)
    
    await update.message.reply_text(
      "Идет подсчет результатов..."
    )
    
    data = await calculate_result(context.user_data)
    
    # db.connect(reuse_if_open=True)
    
    create_test(
      user_id=user.id,
      leader=[x['value'] for x in data if x['type'] == personality_type.LEAD][0],
      shaman=[x['value'] for x in data if x['type'] == personality_type.SHA][0],
      worker=[x['value'] for x in data if x['type'] == personality_type.WORK][0],
      warrior=[x['value'] for x in data if x['type'] == personality_type.WAR][0],
      dealer=[x['value'] for x in data if x['type'] == personality_type.DEAL][0],
      researcher=[x['value'] for x in data if x['type'] == personality_type.RES][0],
      artist=[x['value'] for x in data if x['type'] == personality_type.ART][0],
    )
    
    # db.close()
    
    await sleep(1)
    
    for item in data: 
      output = f"<b>{item['name']} - {item['value']}</b>%\n\n"      
      desc = open(item['description'], 'r')
      output += desc.read()
      
      await update.message.reply_text(
        f"{output}",
        parse_mode='HTML'
      )
      desc.close()
        
    return ConversationHandler.END

def create_answer_markup(data: list[Answer]):
  reply_answers_keyboard = []
  
  for _, item in enumerate(data):
    reply_answers_keyboard.append([item.name])
    
  reply_answers_keyboard.append(["Отмена"])
  
  answer_markup = ReplyKeyboardMarkup(reply_answers_keyboard, resize_keyboard=True)
  
  return answer_markup

def set_default_user_data():
  return { personality_type.LEAD: 0, personality_type.SHA: 0, personality_type.WORK: 0, personality_type.WAR: 0, personality_type.RES: 0, personality_type.DEAL: 0, personality_type.ART: 0, "total": 0 }


# markups
start_markup = ReplyKeyboardMarkup([["Начать", "Отмена"]], resize_keyboard=True, one_time_keyboard=True)

# commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
  """Start the conversation and ask for starting the test"""  
  # db.connect(reuse_if_open=True)
  
  chat_id = update.message.chat_id
  current_user = update.effective_user

  if not user_exists(user_id=current_user.id):
    create_user(id=current_user.id, username=current_user.username, first_name=current_user.first_name, last_name=current_user.last_name, chat_id=chat_id)
      
  # db.close()
  
  await update.message.reply_text("Добрый день!")
  
  start_text = open('assets/description.txt', 'r')

  await update.message.reply_text(
    f"{start_text.read()}",
    parse_mode=ParseMode.HTML
  )
  
  start_text.close()
  
  await sleep(1)
    
  context.user_data['generator'] = generator(questions)
  context.user_data['results'] = set_default_user_data()
  
  await update.message.reply_text(
    "Начать выполнение теста?", 
    reply_markup=start_markup)
  
  return BEGIN

async def attempt_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
  # db.connect(reuse_if_open=True)
  
  chat_id = update.message.chat_id
  current_user = update.effective_user

  if not user_exists(user_id=current_user.id):
    create_user(id=current_user.id, username=current_user.username, first_name=current_user.first_name, last_name=current_user.last_name, chat_id=chat_id)

  # db.close()
  
  context.user_data['generator'] = generator(questions)
  context.user_data['results'] = set_default_user_data()
  
  await update.message.reply_text(
    "Начать выполнение теста?", 
    reply_markup=start_markup)
  
  return BEGIN

async def begin_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:  
  generator = context.user_data['generator']
  (question, current) = next(generator)
  context.user_data['question'] = question
  
  await update.message.reply_text(
    question.name,
    reply_markup=create_answer_markup(question.answers),
  )
  
  return current

async def test_question_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  generator = context.user_data['generator']
  key = await question(update, context, generator)
  return key

async def fallback_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:  
  question = context.user_data['question']
  await update.message.reply_text(
    "Пожалуйста, выберете один из предложенных вариантов. Eсли хотите закончить тест - нажмите кнопку Отмена или команду /cancel", 
    reply_markup=create_answer_markup(question.answers)
  )
  return

async def cancel_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:  
  await update.message.reply_text(
    "Вы прервали тест. Ну что ж, возвращайтесь скорее. Для прохождения теста нажмите /attempt. Команда /help",
    reply_markup=ReplyKeyboardRemove()
  )
  return ConversationHandler.END
  
async def description_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
  start_text = open('assets/description.txt', 'r')

  await update.message.reply_text(
    f"{start_text.read()}",
    parse_mode=ParseMode.HTML
  )
  
  start_text.close()
  
  await update.message.reply_text(
    "Чтобы начать прохождение теста - /attempt"
  )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
  await update.message.reply_text(
    "/start - Начать тест\n/attempt - Начать тест\n/cancel - Прервать тест\n/description - Описание теста\n/bots - Список ботов\n/help - Помощь" 
  )

async def bots_command(update: Update, contex: ContextTypes.DEFAULT_TYPE) -> int:
  list_of_bots = """1. <b>Бросаться снежками</b> - @throw_snowball_bot\n2. <b>Сколько сантиметров?</b> - @pe_size_bot\n3. <b>Last.FM bot</b> - @lastfm_tgbot\n4. <b>Личностый тест</b> - @five_factor_model_bot\n\nПо интересующим вопросам, @keeeparis"""

  return await update.message.reply_text(
    list_of_bots,
    parse_mode=ParseMode.HTML
  )
