const let1 = 12; // глобальная переменная

export default function Example() {
  // функция без аргументов (параметров) и без возврата
  function hello() {
    // camelCase - глагол
    console.log("Hello World");
  }
  // console.log(hello()); // undefined === None

  let num7 = 11; // локальная(блочная) переменная
  // функция с аргументами (параметрами)
  function sum1(a, b) {
    let num8 = 12; // локальная(блочная) переменная
    return a + b;
  }
  // console.log(sum1(12, 13));

  // function expression - функциональное выражение (контекст this - свой)
  const exprFunc = function (a, b) {
    return a + b;
  };
  // console.log(exprFunc(12, 13));

  // array function - стрелочная функция // lambda (контекст this - внешний)
  const arrayFunc = (a, b) => {
    return a + b;
  };
  // console.log(arrayFunc(333, 666));


  // callback - вызов функции - передача функции по ссылке
  function first() {
    setTimeout(function () {
      console.log(1);
    }, 500);
  }
  function second(val) {
    console.log(2);
    console.log(val);
  }
  // first();
  // second();

  function five(firstFunc, SecondFunc){
    firstFunc();
    SecondFunc();
  }
  // five(first, second);

  function third(callbackFunc) {
    console.log(1);
    callbackFunc(666);
  }
  third(second);

    return <div>5Functions.js</div>
}
