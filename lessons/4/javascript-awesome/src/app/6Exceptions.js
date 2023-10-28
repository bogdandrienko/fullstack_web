export default function Example() {
  // exceptions
  const data1 = { name: "test" };
  // console.log(data1.age.length);
  try {
    console.log(data1.age.length);
  } catch (error) {
    console.error("Ошибка:");
    console.log(error);
  } finally {
    console.log("finally");
  }

  return <div>6Exceptions.js</div>
}
