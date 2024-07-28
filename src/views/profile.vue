<template>
  <div class="profile-view">
    <Header />
    <main class="content">
      <h1>FAQ</h1>
    </main>
    <Footer />
  </div>
</template>

<script>
import Header from '@/components/header.vue';
import Footer from '@/components/footer.vue';

export default {
  components: {
    Header,
    Footer,
  },
  methods: {
    goToCatalog() {
      this.$router.push('/catalog');
    },
  },
};
</script>

<style scoped>
/* Стили для вашего компонента */
</style>
