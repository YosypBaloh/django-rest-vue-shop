<script>
import { RouterView } from 'vue-router';

export default {
      data () {
          return {
              basket: []
          }
      },
      methods: {
        addToBasket(item) {
          let found = false 
          this.basket.forEach(el => {
            if(el.slug == item.slug)
              found = true
              return
          })
          if(found) return

          this.basket.push(item)
          localStorage.setItem("basket", JSON.stringify(this.basket))
        },
        deleteFromBasket(slug) {
          this.basket = this.basket.filter(el => {
            return el.slug != slug
          })

          localStorage.setItem("basket", JSON.stringify(this.basket))

        }
      },
  
      created() {
          const savedBasket = localStorage.getItem("basket") || "[]";
          this.basket = JSON.parse(savedBasket);
      }
  }
</script>

<template>
  <div class="container">
      <RouterView :basket="basket" :addToBasket="addToBasket" :deleteFromBasket="deleteFromBasket"/>
  </div>
</template>

<style scoped>

</style>
