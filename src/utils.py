# question_types = ["common", "special", "situation"]
# personality_types = ["leader", "shaman", "worker", "warrior", "dealer", "researcher", "artist"]

class QuestionType:
  def __init__(self):
    self.COMMON = 'common'
    self.SPECIAL = 'special'
    self.SITUATION = 'situation'

class PersonalityType:
  def __init__(self):
    self.LEAD = "leader"
    self.SHA = "shaman"
    self.WORK = "worker"
    self.WAR = "warrior"
    self.DEAL = "dealer"
    self.RES = "researcher"
    self.ART = "artist"

class Answer:
  def __init__(self, name: str, type: str, value: int):
    self.name = name
    self.type = type
    self.value = value

class Question:
  def __init__(self, name: str, question_type: str, answers: list[Answer]):
    self.name = name
    self.question_type = question_type
    self.answers = answers

class ResultVariant:
  def __init__(self, number: int, description: str):
    self.number = number
    self.description = description

class Result:
  def __init__(self, name: str, type: PersonalityType, variants: list[ResultVariant]):
    self.name = name
    self.type = type
    self.variants = variants

personality_type = PersonalityType()
question_type = QuestionType()

questions = [
  Question('Что вам нравится больше?', question_type.COMMON, [
    Answer("Объединять людей", personality_type.LEAD, 3),
    Answer("Помогать (людям, животным, планете)", personality_type.SHA, 3),
    Answer("Создавать что-то полезное", personality_type.WORK, 3),
    Answer("Побеждать", personality_type.WAR, 3),
    Answer("Договариваться", personality_type.DEAL, 3),
    Answer("Изучать новое", personality_type.RES, 3),
    Answer("Быть в центре внимания", personality_type.ART, 3),
  ]),
  Question('Выберите ваш основной талант', question_type.COMMON, [
    Answer("Харизма", personality_type.LEAD, 3),
    Answer("Интуиция", personality_type.SHA, 3),
    Answer("Усердие", personality_type.WORK, 3),
    Answer("Упорство", personality_type.WAR, 3),
    Answer("Находчивость", personality_type.DEAL, 3),
    Answer("Любознательность", personality_type.RES, 3),
    Answer("Артистизм", personality_type.ART, 3),
  ]),
  Question('В чём ваше главное достоинство?', question_type.COMMON, [
    Answer("Лидерство (дипломатия, дисциплина, самоконтроль)", personality_type.LEAD, 3),
    Answer("Открытое сердце (эмпатия, проницательность, прозорливость)", personality_type.SHA, 3),
    Answer("Организованность (пунктуальность, сосредоточенность, практичность)", personality_type.WORK, 3),
    Answer("Целеустремлённость (решительность, настойчивость, дисциплина)", personality_type.WAR, 3),
    Answer("Прагматизм (дипломатия, расчётливость, практичность)", personality_type.DEAL, 3),
    Answer("Рациональность (рассудительность, здравомыслие, реализм)", personality_type.RES, 3),
    Answer("Креативность (яркость личности, неординарность, творческий подход)", personality_type.ART, 3),
  ]),
  Question('Что вам необходимо для успеха?', question_type.COMMON, [
    Answer("Командная работа и дисциплина", personality_type.LEAD, 3),
    Answer("Спокойствие и мудрость", personality_type.SHA, 3),
    Answer("Терпение и труд", personality_type.WORK, 3),
    Answer("Дисциплина и воля", personality_type.WAR, 3),
    Answer("Возможности и связи", personality_type.DEAL, 3),
    Answer("Возможности и опыт", personality_type.RES, 3),
    Answer("Востребованность и смелость", personality_type.ART, 3),
  ]),
  Question('Что самое главное в жизни?', question_type.COMMON, [
    Answer("Единство и процветание", personality_type.LEAD, 3),
    Answer("Любовь и поддержка", personality_type.SHA, 3),
    Answer("Процветание и труд", personality_type.WORK, 3),
    Answer("Справедливость и честь", personality_type.WAR, 3),
    Answer("Отношения и деньги", personality_type.DEAL, 3),
    Answer("Знания и польза", personality_type.RES, 3),
    Answer("Признание и слава", personality_type.ART, 3),
  ]),
  Question('Что главное в людях?', question_type.COMMON, [
    Answer("Ответственность и честность", personality_type.LEAD, 3),
    Answer("Искренность и доброта", personality_type.SHA, 3),
    Answer("Трудолюбие и честность", personality_type.WORK, 3),
    Answer("Решительность и смелость", personality_type.WAR, 3),
    Answer("Богатство и статус", personality_type.DEAL, 3),
    Answer("Открытость к новому", personality_type.RES, 3),
    Answer("Выразительность и стиль", personality_type.ART, 3),
  ]),
  Question('Выберите ваш самый главный приоритет', question_type.COMMON, [
    Answer("Прогресс (эволюция личности и общества)", personality_type.LEAD, 3),
    Answer("Счастье (гармония в сердце, радость и любовь к близким)", personality_type.SHA, 3),
    Answer("Процветание (благоустройство жизни, благополучие и удовлетворение результатом своего труда)", personality_type.WORK, 3),
    Answer("Успех (достижение целей и победа во всём)", personality_type.WAR, 3),
    Answer("Деньги (постоянное увеличение дохода и азарт от получения прибыли)", personality_type.DEAL, 3),
    Answer("Опыт (жажда познания, поиск нового и радость открытия)", personality_type.RES, 3),
    Answer("Признание (известность, востребованность и одобрение публики)", personality_type.ART, 3),
  ]),
  Question('Что из нижеперечисленного у вас получается лучше всего?', question_type.COMMON, [
    Answer("Понимать, кто на что способен, и на основе этого делегировать задачи", personality_type.LEAD, 3),
    Answer("Помогать людям и животным, делать добро", personality_type.SHA, 3),
    Answer("Шаг за шагом благоустраивать свою жизнь", personality_type.WORK, 3),
    Answer("Отстаивать справедливость и добиваться поставленной цели", personality_type.WAR, 3),
    Answer("Договариваться и продавать", personality_type.DEAL, 3),
    Answer("Анализировать ситуации, раскрывать новые грани себя и познавать мир", personality_type.RES, 3),
    Answer("Впечатлять и вдохновлять", personality_type.ART, 3),
  ]),
  Question('Выберите наиболее подходящую для вас историческую фигуру', question_type.COMMON, [
    Answer("Гай Юлий Цезарь", personality_type.LEAD, 3),
    Answer("Серафим Саровский", personality_type.SHA, 3),
    Answer("Томас Эдисон", personality_type.WORK, 3),
    Answer("Александр Македонский", personality_type.WAR, 3),
    Answer("Джон Дэвисон Рокфеллер", personality_type.DEAL, 3),
    Answer("Леонардо да Винчи", personality_type.RES, 3),
    Answer("Фредди Меркьюри", personality_type.ART, 3),
  ]),
  Question('Какое высказывание вам ближе всего?', question_type.COMMON, [
    Answer("Один за всех, и все за одного!", personality_type.LEAD, 3),
    Answer("Слушай своё сердце", personality_type.SHA, 3),
    Answer("Терпение и труд всё перетрут", personality_type.WORK, 3),
    Answer("Дисциплина – мать победы!", personality_type.WAR, 3),
    Answer("Хочешь жить – умей вертеться!", personality_type.DEAL, 3),
    Answer("Ученье – свет, а неученье – тьма", personality_type.RES, 3),
    Answer("Красота требует жертв", personality_type.ART, 3),
  ]),
  
  
  
  Question('Нравится ли вам руководить рабочим процессом?', question_type.SPECIAL, [
    Answer("Я привык всё держать под контролем, люди прислушиваются ко мне", personality_type.LEAD, 3),
    Answer("Мне больше нравится делегировать задачи", personality_type.LEAD, 1),
    Answer("Мне нравится, когда всё идёт по моему плану, но я не сказал бы, что люблю руководить", personality_type.LEAD, 0),
    Answer("Мне легче выполнять какие-то задачи, чем управлять рабочим процессом", personality_type.LEAD, 0),
  ]), 
  Question('Насколько вы харизматичны?', question_type.SPECIAL, [
    Answer("Я люблю объединять людей. Люди всегда поддерживают мою инициативу", personality_type.LEAD, 3),
    Answer("Друзья говорят, что я – душа компании", personality_type.LEAD, 1),
    Answer("У меня много друзей и знакомых, но инициатива не всегда на моей стороне", personality_type.LEAD, 0),
    Answer("Я не особо люблю выделяться, мне больше нравится быть наедине с собой", personality_type.LEAD, 0),
  ]), 
  Question('Насколько хорошо вы понимаете чувства других людей?', question_type.SPECIAL, [
    Answer("Я очень чуткий человек. Понимаю людей с полуслова. Всегда ставлю себя на место другого", personality_type.SHA, 3),
    Answer("Я довольно неплохо понимаю людей. Если дело касается близких, могу искренне посочувствовать и поддержать", personality_type.SHA, 1),
    Answer("Я не могу сказать, что хорошо разбираюсь в людях. Мне сложно сразу понять, что у человека за душой", personality_type.SHA, 0),
    Answer("Честно говоря, чувства людей меня не особо беспокоят", personality_type.SHA, 0),
  ]), 
  Question('Насколько вы любите мир во всём его многообразии (человечество, законы природы, плотность материи)?', question_type.SPECIAL, [
    Answer("Я счастлив, что родился на Земле, и всегда стараюсь сохранять покой в душе и радость в сердце. В любом случае в мире всё справедливо", personality_type.SHA, 3),
    Answer("Я люблю этот мир и верю, что в итоге у всех всё будет хорошо", personality_type.SHA, 1),
    Answer("В принципе, я люблю этот мир. Но иногда мне грустно от того, что в нём так много плохого", personality_type.SHA, 0),
    Answer("Не вижу смысла отвечать на этот вопрос. Мы все и так прекрасно понимаем, в каком мире мы живём...", personality_type.SHA, 0),
    Answer("Я нормалью отношусь к миру и к людям, но только до тех пор, пока кто-то не переступит мои личные границы!", personality_type.WAR, 1),
    Answer("В этом мире столько несправедливости! Я сделаю всё возможное, чтобы навести здесь порядок!", personality_type.WAR, 3),
  ]), 
  Question('Какое место в вашей жизни занимает физический труд?', question_type.SPECIAL, [
    Answer("Это именно то, что позволяет мне чувствовать себя по-настоящему живым", personality_type.WORK, 3),
    Answer("Мне нравится чувствовать в теле приятную усталость в конце дня, но я не могу сказать, что люблю физический труд больше всего", personality_type.WORK, 1),
    Answer("В принципе, я не против поработать физически, но по возможности я бы хотел заниматься этим как можно реже", personality_type.WORK, 0),
    Answer("Я всегда занимаюсь этим через силу", personality_type.WORK, 0),
  ]), 
  Question('Если вы занимаетесь тем, что нравится, насколько для вас важно увидеть результат?', question_type.SPECIAL, [
    Answer("Для меня это очень важно. Я испытываю настоящее удовлетворение, когда работа доведена до конца", personality_type.WORK, 3),
    Answer("Любой положительный результат, пусть даже небольшой, – это именно то, что всегда меня мотивирует", personality_type.WORK, 1),
    Answer("Если это моё любимое дело, я поработаю немножко, а потом займусь чем-то другим. Продолжу, когда будет настроение", personality_type.WORK, 0),
    Answer("У меня нет особого устремления увидеть результат, так как мне просто нравится этим заниматься", personality_type.WORK, 0),
  ]), 
  Question('Насколько для вас важно достигнуть поставленной цели?', question_type.SPECIAL, [
    Answer("Я изо всех сил буду добиваться поставленной цели! И я добьюсь её во что бы то ни стало!", personality_type.WAR, 3),
    Answer("Я сделаю всё возможное для достижения цели. И если ничего не получится, я всё начну сначала", personality_type.WAR, 1),
    Answer("Я сделаю всё возможное для достижения цели. Но если не получится, то я переключусь на что-то другое", personality_type.WAR, 0),
    Answer("Если честно, я не особо люблю чего-то добиваться. Мне больше нравится спокойно плыть по течению", personality_type.WAR, 0),
  ]), 
  Question('Как часто в общении с посторонними людьми вы рассчитываете на личную выгоду?', question_type.SPECIAL, [
    Answer("Я за взаимовыгодное общение", personality_type.DEAL, 3),
    Answer("Мне просто нравится общаться с людьми. Это меня заряжает!", personality_type.DEAL, 1),
    Answer("Если честно, мне всегда трудно разобраться, что выгодно, а что нет", personality_type.DEAL, 0),
    Answer("Когда я общаюсь с людьми, я никогда не думаю выгоде", personality_type.DEAL, 0),
  ]), 
  Question('Как вы относитесь к организационной деятельности?', question_type.SPECIAL, [
    Answer("Положительно. Мне нравится «разруливать» такие задачи", personality_type.DEAL, 3),
    Answer("Могу поработать, но только за хорошие деньги", personality_type.DEAL, 1),
    Answer("Если будет необходимость срочно что-то организовать, я, конечно, сделаю это... Но через силу", personality_type.DEAL, 0),
    Answer("Я избегаю организационных моментов. Это совсем не моё", personality_type.DEAL, 0),
  ]), 
  Question('Нравится ли вам изучать что-то новое?', question_type.SPECIAL, [
    Answer("Для меня это самое интересное в жизни. Мне нравится искать ответы и находить решения", personality_type.RES, 3),
    Answer("Да, мне интересно открывать для себя что-то новое. Я трачу на это много свободного времени", personality_type.RES, 1),
    Answer("Да, мне интересно открывать для себя что-то новое, но у меня есть интересы и поважнее", personality_type.RES, 0),
    Answer("Если честно, мне кажется, это скучно", personality_type.RES, 0),
  ]), 
  Question('Важно ли вам знать причину происходящих в вашей жизни событий?', question_type.SPECIAL, [
    Answer("Конечно, для меня очень важно знать причину. Без этого в моей жизни был бы хаос", personality_type.RES, 3),
    Answer("Я, конечно, иногда задаюсь вопросом «Почему?». Но далеко не всегда", personality_type.RES, 1),
    Answer("Не вижу смысла искать какие-то причины. Что было, то прошло", personality_type.RES, 0),
    Answer("Я вообще привык всё делать на авось", personality_type.RES, 0),
  ]), 
  Question('Как вы относитесь к выступлению на публике? Нравится ли вам быть в центре внимания?', question_type.SPECIAL, [
    Answer("Я рождён, чтобы быть в центре внимания! Да будет шоу!", personality_type.ART, 3),
    Answer("Да, я люблю быть в центре внимания. Но чтобы где-то выступить, мне приходится сделать огромное усилие над собой", personality_type.ART, 1),
    Answer("Я, конечно, люблю внимание окружающих, но публичные выступления – это не для меня", personality_type.ART, 0),
    Answer("Я всегда, наоборот, стараюсь ничем не выделяться. Не хочу быть у всех на виду", personality_type.ART, 0),
  ]), 
  Question('Насколько вам важно то, что о вас подумают другие?', question_type.SPECIAL, [
    Answer("Для меня репутация дороже всего на свете!", personality_type.ART, 3),
    Answer("Конечно, мне важно мнение окружающих, но не до такой степени, чтобы комплексовать по этому поводу", personality_type.ART, 1),
    Answer("Я очень боюсь, что обо мне подумают плохо", personality_type.ART, 0),
    Answer("Чужое мнение меня мало волнует", personality_type.ART, 0),
  ]), 
  
  
  

  Question('Если за окном непогода, и нет никаких срочных дел, что вы будете делать, оставшись дома в одиночестве?', question_type.SITUATION, [
    Answer("Буду решать серьёзные вопросы, планировать завтрашний день, подводить итоги текущего", personality_type.LEAD, 3),
    Answer("Позвоню близким, спрошу, как у них дела", personality_type.SHA, 3),
    Answer("Буду заниматься делами по дому", personality_type.WORK, 3),
    Answer("Развяжу горячий спор в соц-сетях", personality_type.WAR, 3),
    Answer("Буду созваниваться с клиентами", personality_type.DEAL, 3),
    Answer("Буду изучать то, что мне интересно", personality_type.RES, 3),
    Answer("[Займусь творчеством] или [Буду делать посты в соц-сетях, ждать лайки и комментарии]", personality_type.ART, 3),
  ]),
  Question('Если выиграете в лотерею крупную сумму денег, на что потратите?', question_type.SITUATION, [
    Answer("Основную часть этих денег я вложу в своё дело, а остальное отдам на благотворительность", personality_type.LEAD, 3),
    Answer("Не в деньгах счастье. Лучше я отдам их своих близким. Пусть радуются. Мне больше ничего не нужно", personality_type.SHA, 3),
    Answer("Я потрачу эти деньги на благоустройство своей жизни", personality_type.WORK, 3),
    Answer("Я рискну и вложу всё в исполнение своей мечты!", personality_type.WAR, 3),
    Answer("Я вложу деньги в рекламу своих товаров и услуг. Или инвестирую во что-нибудь", personality_type.DEAL, 3),
    Answer("Я потрачу эти деньги на то, что принесёт мне яркий опыт и новые знания", personality_type.RES, 3),
    Answer("Я вложу всё в продвижение себя", personality_type.ART, 3),
  ]),
  Question('Если в ответ на вашу идею собеседник говорит вам: «Это невозможно», что первое приходит вам на ум?', question_type.SITUATION, [
    Answer("Собеседник некомпетентен", personality_type.LEAD, 3),
    Answer("У собеседника просто недостаточно веры", personality_type.SHA, 3),
    Answer("Смотря насколько он разбирается в этом вопросе. Если он – мастер, то я прислушаюсь и оставлю эту затею", personality_type.WORK, 3),
    Answer("Сложно… Но возможно!", personality_type.WAR, 3),
    Answer("Если дело стоит того, то нужно постараться сделать всё возможное. Должен же быть какой-то способ?", personality_type.DEAL, 3),
    Answer("Вопрос недостаточно изучен", personality_type.RES, 3),
    Answer("Мне будет неприятно, что мою идею не поддержали…", personality_type.ART, 3),
  ]),
  Question('Допустим, вы не нарочно задели чувства близкого вам человека, и он обиделся на вас. Как вы поступите?', question_type.SITUATION, [
    Answer("Я вежливо узнаю, как поступать с ним нельзя. Если есть какая-то проблема, я постараюсь найти компромисс", personality_type.LEAD, 3),
    Answer("Я попрошу прощения от всего сердца и постараюсь загладить свою вину", personality_type.SHA, 3),
    Answer("Лучше не обострять конфликт. Я сделаю вид, что ничего не заметил, и вернусь к своим делам", personality_type.WORK, 3),
    Answer("Обиделся? Это не моя проблема! На обиженных воду возят! Я ни в чём не виноват!", personality_type.WAR, 3),
    Answer("Я проявлю дипломатию и объясню человеку, что обижаться не стоит", personality_type.DEAL, 3),
    Answer("Я молча сделаю вывод, как поступать с ним нельзя, и буду постоянно держать это в уме", personality_type.RES, 3),
    Answer("Я напомню этому человеку, почему он меня любит, и за что люблю его я. И он тут же забудет все свои обиды", personality_type.ART, 3),
  ]),
  Question('Вы совершили какую-то оплошность, и вам на это указали. Ваша реакция.', question_type.SITUATION, [
    Answer("Если на ошибку мне указывает человек равный мне или выше по социальному статусу или возрасту, я прислушаюсь", personality_type.LEAD, 3),
    Answer("Я призна́ю, что допустил ошибку, и поблагодарю того, кто мне на неё указал. Ошибки – это рост", personality_type.SHA, 3),
    Answer("Неприятно, конечно... Но я приму это как факт и вернусь к своим делам", personality_type.WORK, 3),
    Answer("Если мне указывает на ошибку равный или ниже по статусу, я защищаюсь; если старший, прислушиваюсь.", personality_type.WAR, 3),
    Answer("Я это как-нибудь обыграю в свою пользу. Или просто переведу всё в шутку", personality_type.DEAL, 3),
    Answer("Я буду искать причину, размышлять день или два, пока не найду ответ, чтобы исключить повторение ошибки. Ошибок быть не должно.", personality_type.RES, 3),
    Answer("Мне станет стыдно, и я промолчу... Я не подам вида. Может, даже улыбнусь. Но в душе я надолго затаю обиду на того, кто сделал мне замечание!", personality_type.ART, 3),
  ]),
  Question('Ваш друг пригласил вас на встречу, а сам опоздал на полчаса. Как вы отреагируете?', question_type.SITUATION, [
    Answer("Я вежливо выскажу ему, что он доставил мне неудобства, и попрошу в следующий раз быть пунктуальнее", personality_type.LEAD, 3),
    Answer("Я закрою на это глаза. Всякое бывает. Главное – пришёл ведь! Друзей надо прощать. Не нужно зацикливаться на мелочах", personality_type.SHA, 3),
    Answer("Я поинтересуюсь, почему он задержался, стараясь не выказывать, что мне это неприятно", personality_type.WORK, 3),
    Answer("Я предъявлю ему претензию. Не люблю, когда меня заставляют ждать. Это несправедливо по отношению ко мне!", personality_type.WAR, 3),
    Answer("Я скажу ему, что раз он опоздал, то он угощает!", personality_type.DEAL, 3),
    Answer("Его опоздание не мешает, наедине мне комфортно. Займусь чтением на телефоне, но важно узнать причину", personality_type.RES, 3),
    Answer("Я очень обижусь на такое отношение ко мне! Буду ждать сердечных извинений и надеяться на то, что причина его опоздания была уважительной", personality_type.ART, 3),
  ]),
  Question('Вам нужно посадить дерево. Ваши действия.', question_type.SITUATION, [
    Answer("Я организую людей и проконтролирую, чтобы дерево было посажено так, как мне нужно", personality_type.LEAD, 3),
    Answer("Я посажу деревце со всей душой, удобрю его, полью, позабочусь, чтобы земля была мягкой и пушистой", personality_type.SHA, 3),
    Answer("Я сделаю эту работу хорошо. Дерево вырастет здоровым", personality_type.WORK, 3),
    Answer("Сделаю всё, чтобы посадить дерево, даже с камнями. Вытащу их и добавлю нормальную землю", personality_type.WAR, 3),
    Answer("Я договорюсь, чтобы кто-нибудь сделал это за меня", personality_type.DEAL, 3),
    Answer("Изучу процесс, выберу место, выкопаю яму, посажу дерево в центр, проверю ровность ствола со всех сторон.", personality_type.RES, 3),
    Answer("Я не буду этого делать. Такая работа не для меня", personality_type.ART, 3),
  ]),
  Question('Вы потеряли какую-то ценную вещь. Ваша реакция.', question_type.SITUATION, [
    Answer("Если вещь памятная, я обращусь в бюро находок и доверю это дело специалистам. А если нет, то я просто куплю себе новую", personality_type.LEAD, 3),
    Answer("Буду спрашивать помощи, и если не найду, ну что поделаешь, вещи приходят и уходят", personality_type.SHA, 3),
    Answer("Я буду искать. Пойду туда, где был. Буду ходить кругами, наклоняться, присматриваться. Если не найду, то очень сильно расстроюсь", personality_type.WORK, 3),
    Answer("Нужно найти любым способом! Сначала позову друзей, если не получится, расклею объявления с предложением вознаграждения", personality_type.WAR, 3),
    Answer("Я поспрашиваю у людей, не находили ли. Если это не принесёт результата, я просто махну рукой и уже завтра про это забуду", personality_type.DEAL, 3),
    Answer("Не паниковать. Сделаю план для поиска, если вещь важна. В противном случае, предприму меры, чтобы не повторилось", personality_type.RES, 3),
    Answer("Спокойствие! Попытаюсь вспомнить, где последний раз видел вещь. Если не найду, буду разыскивать. Ненавижу потери!", personality_type.ART, 3),
  ]),
  Question('Вы получили достоверную информацию, которая опровергла то, в чём ранее вы были убеждены. Ваша реакция.', question_type.SITUATION, [
    Answer("Я приму это как факт. Надо быть гибким и быстро адаптироваться к новому", personality_type.LEAD, 3),
    Answer("Здорово, что мои глаза открылись", personality_type.SHA, 3),
    Answer("Мне всё равно. Все мы ошибаемся", personality_type.WORK, 3),
    Answer("Я мгновенно подстроюсь под это и буду доказывать, что я так и думал всегда", personality_type.WAR, 3),
    Answer("Не мог ошибиться. Истина относительна, точки зрения меняются. Я просто видел с другой стороны", personality_type.DEAL, 3),
    Answer("Обрадуюсь осознанию ошибки, но расстроюсь, нужно будет пересмотреть свою картину мира и адаптироваться", personality_type.RES, 3),
    Answer("То, во что я верил, оказалось иллюзией... Как теперь верить во что-то? Мой мир уже никогда не будет прежним...", personality_type.ART, 3),
  ]),
  Question('Вы создали что-то, на ваш взгляд, поистине ценное (написали отличную книгу, создали прекрасную вещь, сделали научное открытие, придумали гениальную бизнес-идею и т.д.). Затем вы предложили это какой-то крупной компании, но вам отказали. Ваши действия.', question_type.SITUATION, [
    Answer("Мне не нужна их компания. Я создам команду профессионалов и сам реализую свою идею.", personality_type.LEAD, 3),
    Answer("Значит, это просто не мой путь. Возможно, мне уготовано что-то лучше.", personality_type.SHA, 3),
    Answer("Подумаю, что, видимо, вещь не так ценна. Попытаюсь или создам что-то лучше", personality_type.WORK, 3),
    Answer("Глупцы! Я даю вам сокровище! Если вы не возьмёте, другие возьмут!", personality_type.WAR, 3),
    Answer("Отказ – дело обычное. Я просто буду обращаться в другие компании. Если грамотно вести переговоры, то рано или поздно возьмут", personality_type.DEAL, 3),
    Answer("Попрошу перечень недостатков для улучшения. Исходя из этого, устраним ошибки, и решу, обращаться ли снова или искать другую компанию", personality_type.RES, 3),
    Answer("Я очень расстроюсь и [больше никогда не буду этим заниматься] или [скажу им: «Настанет день, и вы ещё пожалеете, что отказались!»]", personality_type.ART, 3),
  ])
]

results = {
  personality_type.LEAD: Result('Вождь (руководитель)', personality_type.LEAD, [
    ResultVariant(100, 'assets/leader/100.txt'),
    ResultVariant(30, 'assets/leader/30.txt'),
    ResultVariant(15, 'assets/leader/15.txt'),
    ResultVariant(7, 'assets/leader/7.txt'),
    ResultVariant(1, 'assets/leader/1.txt'),
    ResultVariant(0, 'assets/leader/0.txt'),
  ]),
  personality_type.SHA: Result('Шаман (созерцатель)', personality_type.SHA, [
    ResultVariant(100, 'assets/shaman/100.txt'),
    ResultVariant(30, 'assets/shaman/30.txt'),
    ResultVariant(15, 'assets/shaman/15.txt'),
    ResultVariant(7, 'assets/shaman/7.txt'),
    ResultVariant(1, 'assets/shaman/1.txt'),
    ResultVariant(0, 'assets/shaman/0.txt'),
  ]),
  personality_type.WORK: Result('Рабочий (созидатель)', personality_type.WORK, [
    ResultVariant(100, 'assets/worker/100.txt'),
    ResultVariant(30, 'assets/worker/30.txt'),
    ResultVariant(15, 'assets/worker/15.txt'),
    ResultVariant(7, 'assets/worker/7.txt'),
    ResultVariant(1, 'assets/worker/1.txt'),
    ResultVariant(0, 'assets/worker/0.txt'),
  ]),
  personality_type.WAR: Result('Воин (достигатор)', personality_type.WAR, [
    ResultVariant(100, 'assets/warrior/100.txt'),
    ResultVariant(30, 'assets/warrior/30.txt'),
    ResultVariant(15, 'assets/warrior/15.txt'),
    ResultVariant(7, 'assets/warrior/7.txt'),
    ResultVariant(1, 'assets/warrior/1.txt'),
    ResultVariant(0, 'assets/warrior/0.txt'),
  ]),
  personality_type.DEAL: Result('Торговец (авантюрист)', personality_type.DEAL, [
    ResultVariant(100, 'assets/dealer/100.txt'),
    ResultVariant(30, 'assets/dealer/30.txt'),
    ResultVariant(15, 'assets/dealer/15.txt'),
    ResultVariant(7, 'assets/dealer/7.txt'),
    ResultVariant(1, 'assets/dealer/1.txt'),
    ResultVariant(0, 'assets/dealer/0.txt'),
  ]),
  personality_type.RES: Result('Исследователь (искатель)', personality_type.RES, [
    ResultVariant(100, 'assets/researcher/100.txt'),
    ResultVariant(30, 'assets/researcher/30.txt'),
    ResultVariant(15, 'assets/researcher/15.txt'),
    ResultVariant(7, 'assets/researcher/7.txt'),
    ResultVariant(1, 'assets/researcher/1.txt'),
    ResultVariant(0, 'assets/researcher/0.txt'),
  ]),
  personality_type.ART: Result('Артист (публичный деятель)', personality_type.ART, [
    ResultVariant(100, 'assets/artist/100.txt'),
    ResultVariant(30, 'assets/artist/30.txt'),
    ResultVariant(15, 'assets/artist/15.txt'),
    ResultVariant(7, 'assets/artist/7.txt'),
    ResultVariant(1, 'assets/artist/1.txt'),
    ResultVariant(0, 'assets/artist/0.txt'),
  ]),
}

