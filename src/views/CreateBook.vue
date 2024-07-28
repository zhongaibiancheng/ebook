<template>
    <v-app>
        <v-row justify="center" align="start">
            <v-col cols="12" md="8">
                <div class="d-flex flex-column align-center justify-center mb-6">
                    <span class="font-weight-bold custom-text-xl block">上传文件制作翻页电子书</span>
                    <span class="custom-text block">支持Pdf,Word,Excel,Ppt,Png,Jpg等格式(100M以内)</span>
                </div>
                <v-card class="mx-auto">
                    <div id="file-input" class="mt-4 mb-4 pl-6 pr-6">
                        <span>选择文件上传(.pdf .doc .xls .jpg .png等)</span>
                        <v-row>
                            <v-col cols="10">
                                <v-file-input accept="image/*" show-size prepend-icon="mdi-file-upload" label="File input"></v-file-input>
                            </v-col>
                            <v-col cols="2">
                                <!-- <v-btn class="ma-2" color="indigo" icon="mdi-cloud-upload"></v-btn> -->
                                <v-btn class="ma-2" color="indigo">
                                    <v-icon icon="mdi-cloud-upload" start></v-icon>
                                    上传
                                </v-btn>
                            </v-col>
                        </v-row>
                        <v-progress-linear v-model="skill" color="blue-grey" height="15" rounded> <template v-slot:default="{ value }">
                                <strong>{{ Math.ceil(value) }}%</strong>
                            </template>
                        </v-progress-linear>
                        <span class="font-weight-black block mt-4 tips">*多个文件会自动合并成一个文件生成电子书</span>
                    </div>
                </v-card>
            </v-col>
        </v-row>
    </v-app>
</template>
<script>
import PdfViewer from '../components/PdfViewer.vue'
export default {
    name: 'Index',
    data: () => {
        return {
            step: 2,
            skill: 20,
        }
    },
    components: {
        PdfViewer: PdfViewer
    },
    methods: {
        gotoPrice() {
            this.$router.push({
                name: 'price'
            })
        },
        gotoBuyDirectly() {
            this.$router.push({
                name: 'buy_directly'
            })
        }
    }
};
</script>
<style scoped>
.custom-text-xl {
    font-size: 1.5rem;
}

.custom-text {
    font-size: 1rem;
}

.block {
    display: block;
}
.tips{
    font-size:0.8rem;
}
</style>