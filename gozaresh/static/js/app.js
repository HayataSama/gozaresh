function copy() {
    var text = document.querySelector('#textarea')
    text.select()
    document.execCommand('copy')
}
var copy_btn = document.querySelector('.copybtn')

copy_btn.addEventListener('click', copy)