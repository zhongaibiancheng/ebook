<template>
    <v-footer app class="bg-indigo-lighten-1 text-center d-flex flex-column">
<!--         <div>
            <v-btn v-for="icon in icons" :key="icon" :icon="icon" class="mx-4" variant="text"></v-btn>
        </div> -->

            <div class="pt-0">
                <strong>众爱编程有限科技公司 2019-2024 </strong>
            </div>
            <v-divider></v-divider>
            ICP-粤xx-009-081

    </v-footer>
</template>
<script>
export default {
    name: 'FooterComponent',
    data: () => ({
        icons: [
            'mdi-facebook',
            'mdi-twitter',
            'mdi-linkedin',
            'mdi-instagram',
        ],
    }),
}
</script>
<style scoped>
v-footer {
    background-color: #3f51b5;
    color: white;
}
</style>