export default function Example() {
  // operators
  // eslint-disable-next-line no-useless-concat
  console.log("arr" + "123");
  console.log(4 - +"123"); // "унарный плюс", знак перед значением
  console.log(4 + "123"); // 4123
  console.log(4 - "123"); // -119


  let a1 = 12;
  let b1 = 12;

  let incr = 10,
    decr = 12;

  console.log(++incr); // префикс увелич
  console.log(incr++); // постфикс увелич
  // for (let i = 0; i < 10; i++) {до или после}

  console.log(--decr); // префикс уменьш
  console.log(decr--); // постфикс уменьш

  console.log(5 > 5);
  console.log(5 < 5);
  console.log(5 >= 5);
  console.log(5 <= 5);
  console.log(5 == "5"); // true сравнение
  console.log(5 === "5"); // false строгое сравнение (типы данных тоже сравниваются)
  console.log(5 != "5"); // отрицание
  console.log(5 !== "5"); // строгое отрицание
  console.log(5 % 2); // остаток от деления
  console.log(true && false); // И (AND)
  console.log(true || false); // ИЛИ (OR)
  console.log(!true); // НЕ (NOT)
  console.log(4 + (2 * 2) === 8); // приоритет операторов (лучше использовать скобки или гуглить)
  // побитовые операторы...

    return <div>2Operators.js</div>
}
