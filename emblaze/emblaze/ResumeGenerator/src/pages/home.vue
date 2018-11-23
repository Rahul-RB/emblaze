<template>
    <div class="home">
        <div class="logo">
            <img src="../assets/logo.jpg" />
        </div>
        <h3 class="title">Click on a resume to preview it!</h3>
        <div class="previews">
            <div class="preview">
                <router-link v-bind:to="'/resume/material-dark'">
                    <div class="preview-wrapper">
                        <img src="../assets/preview/resume-material-dark.png" />
                        <span>material-dark</span>
                    </div>
                </router-link>
            </div>
            <div class="preview">
                <router-link v-bind:to="'/resume/left-right'">
                    <div class="preview-wrapper">
                        <img src="../assets/preview/resume-left-right.png" />
                        <span>left-right</span>
                    </div>
                </router-link>
            </div>
            <div class="preview">
                <router-link v-bind:to="'/resume/oblique'">
                    <div class="preview-wrapper">
                        <img src="../assets/preview/resume-oblique.png" />
                        <span>oblique</span>
                    </div>
                </router-link>
            </div>
            <div class="preview">
                <router-link v-bind:to="'/resume/side-bar'">
                    <div class="preview-wrapper">
                        <img src="../assets/preview/resume-side-bar.png" />
                        <span>side-bar</span>
                    </div>
                </router-link>
            </div>
            <div class="preview">
                <router-link v-bind:to="'/resume/purple'">
                    <div class="preview-wrapper">
                        <img src="../assets/preview/resume-purple.png" />
                        <span>purple</span>
                    </div>
                </router-link>
            </div>
            <div class="preview">
                <router-link v-bind:to="'/resume/side-bar-rtl'">
                    <div class="preview-wrapper">
                        <img src="../assets/preview/resume-side-bar-rtl.png" />
                        <span>side-bar-rtl</span>
                    </div>
                </router-link>
            </div>
            <div class="preview">
                <router-link v-bind:to="'/resume/left-right-rtl'">
                    <div class="preview-wrapper">
                        <img src="../assets/preview/resume-left-right-rtl.png" />
                        <span>left-right-rtl</span>
                    </div>
                </router-link>
            </div>
            <div class="preview">
                <router-link v-bind:to="'/resume/creative'">
                    <div class="preview-wrapper">
                        <img src="../assets/preview/resume-creative.png" />
                        <span>creative</span>
                    </div>
                </router-link>
            </div>
            <div class="preview">
                <router-link v-bind:to="'/resume/cool'">
                    <div class="preview-wrapper">
                        <img src="../assets/preview/resume-cool.png" />
                        <span>cool</span>
                    </div>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
    import Vue from 'vue';
    export default Vue.component('resume', {
        name: 'app'
    });
</script>

<style scoped>
    .home {
        font-family: 'Roboto' !important;
    }
    
    .logo {
        text-align: center;
    }
    
    .logo img {
        height: 50px;
        margin-top: 40px;
    }
    
    .title {
        font-weight: normal;
        text-align: center;
        width: 100%;
        color: black;
        font-weight: 300;
        font-size: 30px;
        line-height: 110%;
        margin: 1.78rem 0 1.424rem 0;
        margin-top: 0px;
        margin-bottom: 40px;
    }
    
    .previews {
        width: 90%;
        margin-right: auto;
        margin-left: auto;
    }
    
    .preview {
        width: 180px;
        float: left;
        margin-left: 1.5%;
        margin-right: 1.5%;
        margin-bottom: 1.5%;
        box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 1px 5px 0 rgba(0, 0, 0, 0.12), 0 3px 1px -2px rgba(0, 0, 0, 0.2);
        height: 252px;
        overflow: hidden;
    }
    
    .preview-wrapper {
        position: relative;
        background: white;
    }
    
    .preview img {
        width: 100%;
        opacity: 0.5;
        filter: blur(1px);
    }
    
    .preview span {
        position: absolute;
        max-width: 100%;
        font-size: 24px;
        font-weight: 300;
        color: rgba(0, 0, 0, 0.75);
        width: 100%;
        text-align: center;
        display: inline-block;
        top: 50%;
        transform: translateY(-50%);
    }
</style>