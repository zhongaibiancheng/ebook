<template>
    <v-app-bar color="surface-variant" app>
      <!-- <v-app-bar-nav-icon></v-app-bar-nav-icon> -->
      <v-img src="/assets/images/logo.png" alt="Logo" contain max-height="50" class="mr-2 hover-pointer" @click="backToIndex"></v-img>
      <v-toolbar-title>文档转书</v-toolbar-title>

        <v-spacer></v-spacer>
        <v-btn text @click="goTo('price')">购买</v-btn>
        <v-btn text @click="goTo('create_book')">创建电子书</v-btn>
        <v-btn text @click="goTo('contact')">我的文档</v-btn>
        <v-spacer></v-spacer>
        <v-btn text @click="login">登录</v-btn>
        <v-btn outlined @click="signUp">注册</v-btn>
    </v-app-bar>
</template>
<script>
export default {
    name: 'HeaderComponent',
    methods: {
        goTo(page) {
            this.$router.push({ name: page });
        },
        backToIndex(){
          this.$router.push({ name: 'index' });
        },
        login() {
          this.$router.push({ name: 'login' });
        },
        signUp() {
          this.$router.push({ name: 'signin' });
        },
    },
};
</script>
<style scoped>
.hover-pointer{
  pointer:default;
}
.hover-pointer:hover{
  cursor: pointer;
}
</style>