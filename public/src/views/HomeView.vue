<script>
import Header from '@/components/Header.vue';
import MainSection from '@/components/MainSection.vue';

export default {
    props: ['basket'],
    components: {  Header, MainSection  }
}
</script>

<template>
 <div>
    <Header  :basket="basket" />
    <MainSection />
 </div>
</template>
