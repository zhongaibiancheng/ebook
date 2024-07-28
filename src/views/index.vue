<template>
    <v-app>
        <v-row justify="center" align="start" style="border:solid 1px blue;">
            <v-col cols="12" md="8">
                <v-main>
                    <v-container fluid>
                        <v-row>
                            <v-col>
                                <v-stepper :model-value="step">
                                    <v-stepper-header>
                                        <v-stepper-item title="文件上传" value="1" complete></v-stepper-item>
                                        <v-divider></v-divider>
                                        <v-stepper-item title="转化文件" value="2"></v-stepper-item>
                                        <v-divider></v-divider>
                                        <v-stepper-item title="付费" value="3"></v-stepper-item>
                                        <v-divider></v-divider>
                                        <v-stepper-item title="下载或转发" value="4"></v-stepper-item>
                                    </v-stepper-header>
                                </v-stepper>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col>
                                <v-card class="mx-auto" v-if="step === 1">
                                    <div id="file-input" class="mt-4 mb-4 pl-6 pr-6">
                                        <span>选择文件上传</span>
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
                                    </div>
                                </v-card>
                                <v-card class="mx-auto pb-6 pr-6 pl-6" v-if="step === 2">
                                    <PdfViewer></PdfViewer>
                                    <v-row justify="space-around">
                                         <v-btn rounded="lg" size="x-large">下载</v-btn>
                                         <v-spacer></v-spacer>
                                         <v-btn rounded="lg" size="x-large" @click="gotoBuyDirectly">单次购买</v-btn>
                                         <v-btn rounded="lg" size="x-large" @click="gotoPrice">购买套餐</v-btn>
                                    </v-row>
                                </v-card>
                            </v-col>
                        </v-row>
                    </v-container>
                </v-main>
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
    methods:{
        gotoPrice(){
            this.$router.push({
                name:'price'
            })
        },
        gotoBuyDirectly(){
            this.$router.push({
                name:'buy_directly'
            })
        }
    }
};
</script>
<style scoped>
#file-input {}
</style>