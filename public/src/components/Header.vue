<script>

</script>

<template>
    <header>
        <img src="/img/logo.svg" alt="">
        <ul>
            <li><RouterLink to="/" active-class="active">Home Page</RouterLink></li>
            <li><a href="">Products</a></li>
            <li><RouterLink to="/shipping" active-class="active">Shipping & Delivery</RouterLink></li>
            <li><RouterLink to="/about" active-class="active">About Us</RouterLink></li>
            <li><img src="/img/purchase.svg" alt=""></li>
        </ul>
    </header>
</template>

<style scoped>
    header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 50px;
    }

header ul {
    list-style: none;
}

header ul li {
    display: inline-block;
    margin-left: 25px;
    cursor: pointer;
}

header ul li .active{
    padding: 5px 15px;
    background: #B2BAC1;
    border-radius: 20px;
}

header ul li .active:hover {
    color:#fff;
    background: #616569;
}

header ul li a {
    position: relative;
    bottom: 10px;
}

</style>
