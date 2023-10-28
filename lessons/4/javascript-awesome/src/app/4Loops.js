export default function Example() {
    // while
    // let counter1 = 50;
    // while (counter1 < 100){
    //     counter1 += 1; // ++num;
    //     console.log(counter1);
    //     // num++;
    // }

    // do while
    // let num1 = 110;
    // do {
    //     num1 += 1;
    //     console.log(num1);
    // }
    // // eslint-disable-next-line no-lone-blocks
    // while (num1 < 100)
    // {
    //     // num++;
    //     num1 += 1;
    //     console.log(num1);
    // }

    // for
    for (let i = 0; i < 10; i += 1) {
        if (i === 7){
            break; // остановка цикла
        }
        if (i % 2 === 0){
            continue; // пропуск шага
        }
        console.log(i);
    }

    // foreach - метод перебора (цикл по объектам)
    // map - функция для прохода по всем элементам








    return <div>4Loops.js</div>
}
