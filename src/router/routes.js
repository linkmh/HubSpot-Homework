import Vue from 'vue';
import VueRouter from 'vue-router';
import MyHome from '../components/MyHome.vue';

Vue.use(VueRouter);

export default new VueRouter({
    mode:'history',
    routes:[
        {
            path:'/',
            name:'MyHome',
            component: MyHome,
        },

    ],
})