<template>
    <div class="wrapper">
        <img src="/img/main-image.svg" alt="">
        <div>
            <img src="/img/asterics.svg" alt="">
            <h1>Shop</h1>
            <h2>online</h2>
            <h3>now</h3>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
            <button>Начать покупки</button>
        </div>
    </div>
</template>

<script>
export default {}
</script>

<style scoped>
.wrapper {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 150px 0;
}

.wrapper > div {
    margin-left: 150px;
    color: #373845;
}

.wrapper > div h1 {
    font-weight: 400;
    font-size: 90px;
}

.wrapper > div h2, .wrapper > div h3 {
    font-weight: 400;
    font-size: 70px;
}

.wrapper > div h3 {color: #5CDDBC;}

.wrapper > div p {
    font-size: 18px;
    width: 500px;
    margin: 20px 0;
}

.wrapper > div button {
    font-weight: 600;
    font-size: 18px;
    color: #2F323A;
    background: #5CDDBC;
    border-radius: 25px;
    border: 0;
    padding: 15px 25px;
    cursor: pointer;
}

.wrapper > div button:hover {
    transform: translateY(-5px);
}
</style>