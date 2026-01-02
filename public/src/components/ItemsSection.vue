<template>
    <div class="items">
        <div class="item" v-for="el in items" :key="el.slug">
            <img :src="'/img/' + el.image" :alt="el.title">
            <h3>{{ el.title }}</h3>
            <p>{{ el.desc }}</p>
            <div class="bottom">
                <span>{{ el.price }}$</span>
                <button>Shop now<img src="/img/add-to-basket.svg" :alt="el.title"></button>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
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

.items .item .bottom img {
    cursor: pointer;
    transition: transform 500ms ease;
}

.items .item .bottom img:hover {
    transform: scale(1.3);
}
</style>