<template>
    <v-container>
        <v-row justify="center">
            <v-col cols="12" md="8">
                <v-card>
                    <v-card-title class="headline">购买内容</v-card-title>
                    <v-card-text>
                        <div v-for="(item,index) in product" :key="index" class="pl-3">
                            <span class="text-body-1 font-weight-medium mt-2">{{item.title}}</span>
                            <span class="text-body-1 mt-2">{{item.content}}</span>
                        </div>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
        <v-row justify="center">
            <v-col cols="12" md="8">
                <v-card>
                    <v-card-title class="headline">支付方式</v-card-title>
                    <v-card-text class="pl-4">
                        <v-radio-group v-model="selected" column>
                            <v-radio v-for="(option, index) in options" :key="index" :label="option.label" :value="option.value">
                                <template v-slot:label>
                                    <font-awesome-icon left :icon="option.icon" size="2x" /><span class="pl-3">{{ option.label }}</span>
                                </template>
                            </v-radio>
                        </v-radio-group>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
        <v-row justify="center">
            <v-col cols="12" md="4" sm="6">
                <v-btn size="x-large" block>支付</v-btn>
            </v-col>
        </v-row>
        <!--
        <v-row justify="center">
            <v-col cols="12" md="8">
                <div>
                    <v-divider :thickness="3" color="success"></v-divider>
                </div>
                <div class="mt-2 text--grey">
                    <div class="text-subtitle-2">支付注意事项</div>
                    <ul class="no-bullets">
                        <li class="text-subtitle-2 pl-4">本商品不支持退款</li>
                        <li class="text-subtitle-2 pl-4">支付后方可下载</li>
                    </ul>
                </div>
            </v-col>
        </v-row>
      -->
    </v-container>
</template>
<script>
export default {
    name: 'Payment',
    data: () => {
        return {
            selected: 'user',
            options: [
                { label: '支付宝', value: 'user', icon: ['fab', 'alipay'] },
                { label: '微信', value: 'email', icon: ['fab', 'weixin'] }
            ],
            product: [{
                    title: '商品名称:',
                    content: ' 电子书',
                },
                {
                    title: '价格:',
                    content: ' ￥29.00',
                },
                {
                    title: '描述:',
                    content: '生成的电子书HTML文件包，下载后可以直接使用',
                },
            ]
        }
    }

};
</script>
<style scoped>
.headline {
    font-size: 20px;
    font-weight: bold;
}

.no-bullets {
    list-style-type: none;
    padding-left: 0;
}
</style>