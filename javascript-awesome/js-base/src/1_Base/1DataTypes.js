// "use strict"; // строгий режим, отключает поведение старых версий, например var

export default function Example() {
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
  const string1 = "Hello World"; // строки
  const string2 = "Hello World"; // одинарные кавычки
  const string3 = `Hello World`; // бэктики (косые кавычки)
  const null1 = null; // значения не существует (Referrence error)
  const undefined1 = undefined; // существует, но значения нет
  // symbol, bigint

  // OBJECTS
  const object1 = { name: "JS", age: 25 }; // объекты - словари
  const object2 = { age: 26 }; //
  console.log(object2.age); // getter
  console.log(object2["age"]); // getter (bad practice)
  object2.age = "JS"; // setter

  //                      0   1    2
  const arr1 = [12, 13, 14]; // массивы (частный случай объекта)
  const arr2 = ["12"]; //
  // const arr2: string[] = ["12"]; // work in TYPESCRIPT
  const dateTime1 = new Date(); // дата и время
  // regex, errors, functions...

  // METHODS

  console.log(Math.round(number2));
  console.log(parseInt("10.5px", 10));
  console.log(parseFloat("10.5px"));
  console.log(string3.length);
  console.log(string3.toLowerCase());
  console.log(string3.indexOf("W"));
  console.log(string3.slice(2, 5));
  // console.dir(Number);
  // docs

  // ACTIONS
  // базовый alert
  // alert("Не закрывайте вкладку");

  // базовый input (-> true/false)
  // eslint-disable-next-line no-restricted-globals
  // console.log(confirm("Ты согласен?")) //

  // базовый input (-> string)
  // console.log(prompt("Ты согласен?", "Да"))
  // console.log(+prompt("Ты согласен?", "Да")) // слабая динамическая типизация ->  в число
  // console.log(prompt("Ты согласен?", "Да")+5) // 105

  // вывод на страницу
  // document.write("<h1>Hello World</h1>"); // устарело

  // интерполяция
  // const category1 = "toys";
  // console.log("123" + category1 + '/' + category1 + '/' + category1);
  // console.log(`123${category1}/${category1}/${category1}`);

  // JSX
  return <div>js</div>;
}
