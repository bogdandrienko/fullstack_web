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
  }

  // switch-case
  switch ("Банан") {
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

  20 > 20 && console.log("больше")(20 > 20)
    ? console.log("больше")
    : console.log("меньше");

  return <div>js</div>;
}
