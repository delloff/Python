#slice работает также со string

Маленькое вступление. Уверен, что каждый, кто использовал питон некоторое время, полюбил выражения в прямоугольных скобочках.
В этой статье я хочу от «а» до «я» рассказать о срезах. Для начала немного о терминологии: в английском языке их называют «slice».
Я буду называть их то «слайсами», то «срезами», как в моем понимании этого слова. Будем все учиться на примерах. Для меня,
такой метод был бы самым удобным, быстрым и простым.
Для начала, самое распространенное применение. Создания копии последовательности или ее части.
Рассмотрим срез как часть последовательности. Например, несколько срезов со списка:
  
s = [1, 2, 3, 4, 6, 7] #простой список
s[:] #копия списка, часто очень полезно
[1, 2, 3, 4, 6, 7]
s[1:] # все элементы кроме первого
[2, 3, 4, 6, 7]
s[-3:] # последние 3 элемента
[4, 6, 7]
s[-1] # последний элемент (тоже самое как  [-1:], только не диапазон а один элемент)
[7]
s[-1:]
[7]
s[2:-2] #откидываем первые и последние 2
[3, 4]
s[2:4] #откидываем первые и последние 2
[3, 4]
s[:2] #первых два элемента
[1, 2]
s[:-4] # все элементы за исключением последних 4
[1, 2]




Это ещё не все,
Далеко не все знают, но могут быть слайсы с тремя параметрами:
  
s[::2] #парные элементы
[1, 3, 6]
s[1::2] # парные элементы начиная со второго
[2, 4, 7]
s[1:4:2] #элементы с первого по четвертый с шагом 2
[2, 4]


Все эти действия можно проворачивать со строками, кортежами и списками.
"Hello Dolly!"[1::2]
'el ol!'

Совсем забыл, обратный порядок:
"God saw I was dog"[::-1]
'god saw I was doG'
>>> #отрицательный шаг может оказаться граблями, если не знать особенностей. См комментарии.

Но и это ещё не все, есть несколько действий со срезами, которые можно делать только со списками (ну, почти). Дело в том, что они единственные из базовых последовательностей, которые могут изменяться, и, для которых, имеет значение порядок (нельзя делать срезы из словарей и множеств/наборов). Дальше пойдет разговор о срезах, которые изменяют последовательность.
Слайсы можно удалять, например:
  
s = list(range(10)) #заполняем 0..9
del s[3: -2: 2] #удаляем элементы между третьим и предпоследним с шагом 2
s
[ 0, 1, 2, 4, 6, 8, 9]


Ещё можно вставлять элементы:
В варианте замены:
  
s[2:5:2]=list("AF") #список был [0, 1, 2, 4, 6, 8, 9], мы заменили указанные элементы на [‘A’,’F’]
#да, ещё в такой конструкции должны совпадать размеры, это легче понять попробовав
s
[ 0, 1, 'A', 4, 'F', 8, 9]


Ну, или вариант вставки попроще:
  
s[3:4] = ["4 was here"] # замена последовательного кусочка
s
[ 0, 1, 'A', '4 was here', 'F', 8, 9]
s[1:1] = ["after zero"] #или, просто, вставка
s
[ 0, 'after zero', 1, 'A', '4 was here', 'F', 8, 9]


Если мы хотим создать класс, с которого можно снимать срезы? Проще некуда, для этого есть два пути:
Неправильный:
1) Переопределить фунции __getslice__, __delslice__ и __setslice__. Но это устаревший метод (в 2.0 помечен как deprecated)
И правильный:
2) Переопределить __getitem__, __setitem__ и __delitem__.
С первого взгляда все кажется предельно простым, но если присмотреться, то __getitem__(self, key) – получает только один параметр, key, а у среза у нас может быть целых 3 числа… Все предельно просто: в случае, когда кто-то пытается срезать кусочек от нашего объекта, значением key функция получит объект типа slice:
    
class MySliceble():
def __getitem__(self, key):
    if isinstance(key, slice):
        return list(range(key.start, key.stop, key.step))
    else:
        raise Exception("Trying to access by index")
my = MySliceble()
my[2:10:1]
[2, 3, 4, 5, 6, 7, 8, 9]

Конечно, пример очень символический, но понять можно: у объекта класса slice есть три свойства: start, stop и step, соответствуют числам из скобок среза. Нужно быть внимательным, если число пропущена, то значение будет None, например [::] будет slice(None, None, None) а [:-3] будет slice(None, -3, None).
Замену/вставку и удаление срезов делаем по аналогии.
Как упражнение, можете попробовать перегрузить словарь, чтобы с него можно было делать срезы. В питоне3 это будет начинаться как class SliceableDict(dict):
Ну, вроде все, что есть о срезах.
Если что пропустил с удовольствием выучу и допишу.
