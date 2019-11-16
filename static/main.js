/*jshint esversion: 6 */
var vm = new Vue({
    el: '#app',
    data() {
        return {
            input_text: "",
            hash_text: "",
        };
    },
    methods: {
        hash(input) {
            // $.get("/hash", { 'input_text': this.input_text }, function(ret) {
            //     console.log(ret)
            //     this.hash_text = ret
            // })
            console.log(this.input_text);
            this.$http.get('hash/' + this.input_text)
                .then((response) => {
                    this.hash_text = response;
                    console.log(response);
                    //                     console.log(response.body);
                    $("#hash_text").text(response.body);
                    $("#input")[0].value = "";
                })
                .catch((response) => {
                    console.log(response);

                });

        },
    },
});