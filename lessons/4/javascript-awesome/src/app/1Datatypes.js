// js - javascript
// ts - typescript
// jsx - react (extended javascript)
// tsx - react + typescript

// "use strict"; // строгий режим, отключает поведение старых версий, например var

export default function Example() {
    console.log("Danat");

    let exNumber1 = 5; // изменяемая переменная
    const exNumber2 = 5; // неизменяемая
    var exNumber3 = 5; // изменяемая, инициализация до объявления в коде (устарело)

  console.log(exNumber1);
  console.log(typeof exNumber1);
  console.error("hi!");

  // SIMPLE
  const boolean1 = true; // булевы (правда/ложь)
  const number1 = 12; // числа (+infinity, -infinity, NaN - not a number)
  const number2 = 12.0; // числа
  const number3 = 12000000000000000000000000n; // bigint
  const string1 = "Hello World"; // строки
  const string2 = 'Hello World'; // одинарные кавычки
  const string3 = `Hello World`; // бэктики (косые кавычки)
  const null1 = null; // значения не существует (Referrence error)
  const undefined1 = undefined; // существует, но значения нет
  // symbol

  // OBJECTS
  const object1 = { "name": "JS", age: 25 }; // объекты - словари
  const object2 = { age: 26 }; // ассоциативный массив(ключ-значения)
  console.log(object1);
  console.log(object2.age); // getter
  console.log(object2["age"]); // getter (bad practice)
  object1.name = "PYTHON"; // setter
  console.log(object1);

  //                      0   1    2
  const arr1 = [12, 13, 14]; // массивы (частный случай объекта)
  console.log(arr1[1]);
  const arr2 = ["12"]; //
  // const arr2: string[] = ["12"]; // work in TYPESCRIPT
  const dateTime1 = new Date(); // дата и время
  // regex, errors, functions...

  // METHODS
  console.log(Math.round(number2));
  console.log(parseInt("10.99px", 10));
  console.log(parseFloat("10.99px"));
  console.log(string3.length);
  console.log(string3.toLowerCase());
  console.log(string3.indexOf("W"));
  console.log(string3.slice(2, 5)); // string3[2, 5, 1] - python
  console.dir(String); // docs

  // ACTIONS
  // - react - лучше создавать "модальные окна"

  // базовый alert
  // alert("Не закрывайте вкладку");
  // document.windows.alert(); // react

  // базовый input (-> true/false)
  // eslint-disable-next-line no-restricted-globals
  // console.log(confirm("Ты согласен?")); //

  // базовый input (-> string)
  // console.log(prompt("Ты согласен?", "Да"))
  // console.log(+prompt("Ты согласен?", "ДА")); // -> NAN // слабая динамическая типизация ->  в число
  // console.log(+prompt("Ты согласен?", "11")); // -> 11 // слабая динамическая типизация ->  в число
  // console.log(prompt("Ты согласен?", "100")+5); // '100' + 5 = 1005
  // конвертация типов может происходить неявно

  // вывод на страницу
  // document.write("<h1>Hello World</h1>"); // устарело

  // интерполяция
  const category1 = "toys";
  console.log("123" + category1 + '/' + category1 + '/' + category1 +  '/' + 10); // concatenation
  console.log(`123${category1}/${category1}/${category1}/${10}`); // interpolation

    return <div>1Datatypes.js</div>
}
