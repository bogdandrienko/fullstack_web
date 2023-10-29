export default function Example() {
  // exceptions
  const data1 = { name: "test" };
  // console.log(data1.age.length);
  try {
    console.log(data1.age.length);
  } catch (error) {
    console.error("Ошибка:");
    console.error(error);
  }

  return <div>js</div>;
}
