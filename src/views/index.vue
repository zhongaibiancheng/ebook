<template>
    <v-app>
        <v-row justify="center" align="start" style="border:solid 1px blue;">
            <v-col cols="12" md="8">
                <v-main>
                    <v-container fluid>
                        <v-row>
                            <v-col>
                                <v-stepper model-value="2">
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
                                <div id="file-input" class="mt-2 pl-2 pr-2">
                                    <span>选择文件上传</span>
                                    <v-row>
                                        <v-col cols="10">
                                            <v-file-input accept="image/*" show-size prepend-icon="mdi-file-upload" label="File input"></v-file-input>
                                        </v-col>
                                        <v-col cols="2">
                                            <!-- <v-btn class="ma-2" color="indigo" icon="mdi-cloud-upload"></v-btn> -->

                                            <v-btn
        class="ma-2"
        color="indigo"
      >
        <v-icon
          icon="mdi-cloud-upload"
          start
        ></v-icon>
        上传
      </v-btn>

                                        </v-col>
                                    </v-row>
                                    <v-progress-linear color="blue-lighten-3" model-value="20"></v-progress-linear>
                                </div>
                            </v-col>
                        </v-row>
                    </v-container>
                </v-main>
            </v-col>
        </v-row>
    </v-app>
</template>
<script>
export default {
    name: 'Index',
    data: () => {
        return {

        }
    },
    components: {

    },
};
</script>
<style scoped>
#file-input {}
</style>