<template>
    <v-app>
        <HeaderComponent />
        <FooterComponent />
        <v-main fill-height>
            <router-view />
        </v-main>
    </v-app>
</template>
<script>
import HeaderComponent from './components/Header.vue';
import FooterComponent from './components/Footer.vue';

export default {
    name: 'App',
    components: {
        HeaderComponent,
        FooterComponent,
    },
};
</script>
<style>
</style>