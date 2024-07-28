<template>
  <div class="home-view">
    <Header />
    <main class="content">
      <h1>Главная</h1>
      <p>
        Мы производим мебель из дерева без единого гвоздя. Наша продукция
        экологична и долговечна.
      </p>
      <div class="photos">
        <img src="@/assets/primer1.jpg" alt="Пример мебели 1" />
        <img src="@/assets/primer3.jpg" alt="Пример мебели 2" />
        <img src="@/assets/primer2.jpg" alt="Пример мебели 3" />
      </div>
      <button class="catalog-button" @click="goToCatalog">
        Перейти в каталог!
      </button>
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
.home-view {
  background-color: #fff8e7;
  color: #333;
  text-align: center;
  font-family: Inter;
}

.content {
  max-width: 800px;
  margin: 0 auto;
}

.photos {
  display: flex;
  justify-content: space-around;
  margin: 20px 0;
}

.photos img {
  width: 200px;
  height: auto;
  border-radius: 10px;
}

.catalog-button {
  background-color: #8b4513;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.catalog-button:hover {
  background-color: #a0522d;
}
</style>
