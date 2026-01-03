<template>
    <div class="items">
        <div class="item" v-for="el in items" :key="el.slug">
            <img :src="'/img/' + el.image" :alt="el.title">
            <h3>{{ el.title }}</h3>
            <p>{{ el.desc }}</p>
            <div class="bottom">
                        <span>{{ el.price }}$</span>
            <button @click="addToBasket(el)">Shop now<img src="/img/add-to-basket.svg" :alt="el.title"></button>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    props: ['addToBasket'],
    data() {
        return {
            items: []
        }
    },
    async mounted() {
        try {
            const res = await axios.get('http://127.0.0.1:8000/api/items/?format=json')
            this.items = res.data
        } catch(error) {
            console.log(error)
        }

    }
}
</script>

<style scoped>
.items {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
}

.items .item {
    margin-bottom: 100px;
    width: 350px;
    padding: 15px;
    background: #F4F4F4;
}

.items .item img:first-child {width: 100%;}

.items .item h3 {
    margin: 12px 0;
    font-size: 20px;
}

.items .item p {
    margin: 10px 0;
    font-size: 15px;
    width: 90%;
}

.items .item .bottom {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
}

.items .item .bottom span {
    font-weight: 600;
    color: #216E5B;
}

.items .item .bottom button img {
    width: 20px;
    height: auto;
    transition: transform 0.2s ease;
}
.items .item .bottom button:hover {
    transform: scale(1.15);
}  


.items .item .bottom button {
    background: transparent;
    border: none;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 10px;
    font-weight: 600;
    color: #216E5B;
    font-size: 16px;
    transition: transform 0.5s ease;
}

.items .item .bottom button img {
    width: 22px;
    height: auto;
}
</style>