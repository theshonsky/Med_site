const copyText = [...document.getElementsByClassName('copy-btn')]
  let previous = null
  let last = null
  copyText.forEach(btn=> btn.addEventListener('click', ()=>{
    const number = btn.getAttribute('mkbid')
    console.log(number)
    navigator.clipboard.writeText(number)
    btn.textContent = 'Скопировано'
    
    if (previous){
      previous.textContent= last
    }
    previous = btn
    last = number
  }))