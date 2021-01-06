const DiceButton = ({die, onRoll}) => {
    const handleClick = () => {
        var num1 = get_random_int(die)
        console.log(num1)
        onRoll(num1)
    }
    const get_random_int = (max) => {
        return Math.floor(Math.random() * Math.floor(max)) + 1
    }

    return (
        <button onClick={handleClick}>
            Roll a d{die}
        </button>
    )
}

export default DiceButton
