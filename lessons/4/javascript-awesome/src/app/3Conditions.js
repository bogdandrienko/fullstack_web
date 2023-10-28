export default function Example() {
  // условия

  // only if
  const bool11 = true;
  if (bool11) {
    console.log("true 1");
  }

  // if-else
  if (!bool11) {
    // отрицание
    console.log("true 2");
  } else {
    console.log("false 2");
    if (!bool11) {
      // отрицание
      console.log("true 2");
    } else {
      console.log("false 2");
    }
  }

  const key = "Банан";
  // switch-case
  switch (key) {
    case "Банан": {
      console.log("Банан");
      break;
    }
    default: {
      console.log("default");
      break;
    }
  }

  // тернарный оператор
  // if
  const var1 = 20 >= 20 && 666; // 666 | false
  console.log(var1);

  // if-else
  const var2 = 20 >= 20 ? 666 : 555; // 666 | 555
  console.log(var1);

  20 >= 20 && console.log("больше или равно");

  (20 > 20) ? console.log("больше")
    : console.log("меньше");

    return <div>3Conditions.js</div>
}
