# Проект сделан студентами 27 группы: Терешкин Михаил — Russakura8, Дорофеев Андрей — Allmoon1, Гаврилов Антон — Gorilla73 и Ищенко Андрей — andreyka-konareyka. 

Делая этот проект мы прошли через огонь, воду и медные трубы. Нам пришлось потратить 6 рублей на тестирование оплаты, у нашего ведущего программиста по боту чуть не слетела винда из-за включения виртуализации, нам пришлось заниматься тем, в чём мы, к сожалению, не разбираемся.
Поэтому, чтобы запустить проект, придётся немного потанцевать с бубном (ну без приключений было бы скучно, не правда ли?). 
У нас есть телеграм-бот, сайт и андроид-приложение.
Чтобы запустить сайт нужно прочитать комментарий от главного разработчика сайта:

          "Здесь я объясняю как запустить сайт с помощью докера:
          1) Прописать команду: docker build .
          2) Посмотреть образ под тэгом <none> и скопировать его id
          3) Прописать команду: docker run --rm -d --publish 8000:8000 <id>

          Теперь по функционалу сайта.
          В панели администратора /admin сть возможность добавить категории товаров, сам товар,
          которые автоматически отобразятся на сайте и это потрясающе я считаю. Также есть корзина
          с возможностью добавления, изменения и удаления товара из нее. При оформлении заказа нужно
          заполнить форму, которая отобразится в Orders в панели администратора, так работники смогут
          понять, что и кому нужно готовить

          Возможные проблемы.(Эта ошибка маловероятна, но если возникла то вот решение)
          Вроде как для анонимного пользователя добавление работает корректно,
          но иногда происходят неизвестные мне сбои и как их исправить я не представляю, но если
          такая проблема возникла, то вот способ решения
              Зайти в панель администратора /admin и ввести
                                                  логин:admin
                                                  пароль:qwerty
              Теперь мы авторизованы и никаких проблем и нигде не будет

          Также нет привязки Покупатель-Заказ, потому что в этом случае возникают ошибки, которые я не в силах починить,
          но так как в форме оформления заказа есть данные покупателя, то я думаю я смог выкрутиться из ситуации, ведь в
          панели администратора в Orders видны все данные покупателя."

Чтобы заработало приложение для этого нужно запустить сначала сервер из папочки Server, а потом само приложение: 

          "Так как при упаковке файлов в докер возникли конфликты, придётся провести некоторые настройки, а именно:
          1) Создать в postgres базу данных с именем coffee
          2) В файле application.properties добавить свои имя и пароль в нужные строки
          3) Выполнить программу "Init_DB.py" (для этого понадобится установить модуль requests)
          4) Теперь сервер готов к работе
          5) Переходим к запуску приложения (хоть там и есть апк файл, не нужно его запускать, так как у него почему-то возникают конфликты с библиотекой requests)
             Нам нужно открыть папку Android в любом удобном окружении для запуска программ на python и установить туда версию python 3.9
          6) импортировать библиотеки requests (она уже должна быть импортирована, если до этого был использован файл "Init_DB.py"), kivy_examples и kivy (в процессе работы 
             мы поняли, что надо было выбрать другой фреймворк, но пути назад уже не было (да и язык тоже))
          7) Запустить файл main.py в приложении (чтобы всё заработало, сервер тоже надо запустить перед запуском приложения)
          Возможности:
          В приложении можно зарегистрироваться, использовав номер телефона, и сделать заказ, интересующих вас продуктов из меню."

Блок бот, так как опять-таки при упаковке в докер возникли конфликты предлагается запустить его через любое удобное окружение для работы с python:

          "1) Устанавливаем необходимые библиотеки из файла (requirements.txt) 
          2) Запускаем уже настроенный сервер
          3) Запускаем Telegrasm.py
          4) Идём к боту, которого зовут @GavrilovAnt_bot
          Возможности:
          Бот может показать доступное на данный момент меню (которое есть в бд и "amount" > 0), можно сделать заказ и оплатить его через киви (если вдруг захочется воспользоваться оплатой
          и не захочется тратить >= 50 руб, то можно в коде поменять строку 242 "if zakaz["price"] <= 50:" на "if zakaz["price"] <= 0:" и в бд у чего-нибудь изменить цену на 
          1 рубль ("price"))"

Хоть криво и косо, но с душой (зато своё, родное), мы проделали довольно большую (по нашим ощущениям) работу и готовы с радостью поделиться ей.           
             
