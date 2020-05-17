let mappings = {
  joy: '0x1F60A',
  fear: '0xE40B',
  anger: '0xe059',
  sadness: '0xE058',
  disgust: '0xE406',
  shame: '0xE403',
  guilt: '0xE408',
};

let mappings2 = {
  joy: ':blush:',
  fear: '0xE40B',
  anger: '0xe059',
  sadness: '0xE058',
  disgust: '0xE406',
  shame: '0xE403',
  guilt: '0xE408',
};

document.querySelector('#submit-btn').addEventListener('click', predictEmoji);

function deleteMessage(e) {
  let list = e.target.parentElement.parentElement;
  list.removeChild(e.target.parentElement);
}

function predictEmoji() {
  let inputText = document.querySelector('#input-text').value;
  let list = document.querySelector('#messages-list');
  //console.log(inputText);
  fetch(`http://localhost:5000/${inputText}`)
    .then((res) => res.text())
    .then((text) => {
      //console.log(text);

      document.querySelector('.messages-wrapper').style.display = 'block';

      let newItem = document.createElement('li');
      newItem.append(document.createTextNode(inputText + ' '));

      let emoji = document.createElement('img');
      emoji.src = `../../assets/images/${text}.png`;
      newItem.appendChild(emoji);

      let closeBtn = document.createElement('i');
      closeBtn.className = 'fas fa-times delete';
      closeBtn.addEventListener('click', deleteMessage);
      newItem.appendChild(closeBtn);

      list.insertBefore(newItem, list.children[0]);
      document.querySelector('#input-text').value = '';
    });
}
