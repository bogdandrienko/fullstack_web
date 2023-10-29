export default function Example() {
  // функция без аргументов (параметров) и без возврата
  function hello() {
    // camelCase - глагол
    console.log("Hello World");
  }
  hello();

  let num7 = 12; // глобальная переменная
  // функция с аргументами (параметрами)
  function sum1(a, b) {
    let num8 = 12; // локальная переменная
    return a + b;
  }
  console.log(sum1(12, 13));

  // function expression - функциональное выражение
  const exprFunc = function (a, b) {
    return a + b;
  };

  // array function - стрелочная функция
  const arrayFunc = (a, b) => {
    return a + b;
  };
  console.log(arrayFunc(333, 666));

  // callback
  function first() {
    setTimeout(function () {
      console.log(1);
    }, 500);
  }

  function second() {
    console.log(2);
  }
  first();
  second();

  function third(message, callbackFunc) {
    console.log(message);
    callbackFunc();
  }

  third("3", first);

  return <div>js</div>;
}
