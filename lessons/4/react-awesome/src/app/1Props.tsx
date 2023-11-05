export function Props1(){
    const a  = 12;
    return <div>JSX{a}</div>
}

export default function Props2(){
    const a  = 13;
    return <div>JSX{a}</div>
}

export function Props3({value="888", children}: any){
    return <div>{value} :{children}</div>
}
