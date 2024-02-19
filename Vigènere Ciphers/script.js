// Vigènere Cipher
$(document).ready(function () {
  function vigenereEncrypt(plaintext, key) {
    let encryptedText = "";
    let j = 0;
    let startTime = performance.now();
    let operationCountEncrypt = 0;

    for (let i = 0; i < plaintext.length; i++) {
      let currentChar = plaintext[i];
      if (currentChar.match(/[a-zA-Z]/)) {
        let isUpperCase = currentChar === currentChar.toUpperCase();
        let charCode =
          currentChar.toUpperCase().charCodeAt(0) - "A".charCodeAt(0);
        let keyCode =
          key[j % key.length].toUpperCase().charCodeAt(0) - "A".charCodeAt(0);
        let encryptedCharCode = (charCode + keyCode) % 26;
        encryptedText += isUpperCase
          ? String.fromCharCode(encryptedCharCode + "A".charCodeAt(0))
          : String.fromCharCode(encryptedCharCode + "a".charCodeAt(0));
        j++;
      } else {
        encryptedText += currentChar; // Menambahkan karakter non-alfabet tanpa modifikasi
      }
      operationCountEncrypt++;
    }
    let endTime = performance.now();
    let timeTakenEncrypt = endTime - startTime;
    return { encryptedText, timeTakenEncrypt, operationCountEncrypt };
  }

  function vigenereDecrypt(ciphertext, key) {
    let decryptedText = "";
    let j = 0;
    let startTime = performance.now();
    let operationCountDecrypt = 0;

    for (let i = 0; i < ciphertext.length; i++) {
      let currentChar = ciphertext[i];
      if (currentChar.match(/[a-zA-Z]/)) {
        let isUpperCase = currentChar === currentChar.toUpperCase();
        let charCode =
          currentChar.toUpperCase().charCodeAt(0) - "A".charCodeAt(0);
        let keyCode =
          key[j % key.length].toUpperCase().charCodeAt(0) - "A".charCodeAt(0);
        let decryptedCharCode = (charCode - keyCode + 26) % 26;
        decryptedText += isUpperCase
          ? String.fromCharCode(decryptedCharCode + "A".charCodeAt(0))
          : String.fromCharCode(decryptedCharCode + "a".charCodeAt(0));
        j++;
      } else {
        decryptedText += currentChar; // Menambahkan karakter non-alfabet tanpa modifikasi
      }
      operationCountDecrypt++;
    }
    let endTime = performance.now();
    let timeTakenDecrypt = endTime - startTime;
    return { decryptedText, timeTakenDecrypt, operationCountDecrypt };
  }

  $("#encryptForm").submit(function (e) {
    e.preventDefault();
    let message = $("#message").val();
    let key = $("#key").val();
    let result = vigenereEncrypt(message, key);
    $("#encryptedMessage").html(
      "<span class='fw-bold'>Pesan Terenkripsi: </span>" + result.encryptedText
    );
    $("#encryptionTime").html(
      "<span class='fw-bold'>Waktu Enkripsi: </span>" +
        result.timeTakenEncrypt +
        " milidetik."
    );
    $("#encryptionOperation").html(
      "<span class='fw-bold'>Operasi Enkripsi: </span>" +
        message.length +
        " karakter, " +
        result.operationCountEncrypt +
        " operasi."
    );
  });

  $("#decryptForm").submit(function (e) {
    e.preventDefault();
    let encryptedMessage = $("#encryptedMessageInput").val();
    let key = $("#keyInput").val();
    let result = vigenereDecrypt(encryptedMessage, key);
    $("#decryptedMessage").html(
      "<span class='fw-bold'>Pesan Terdekripsi: </span>" + result.decryptedText
    );
    $("#decryptionTime").html(
      "<span class='fw-bold'>Waktu Dekripsi: </span>" +
        result.timeTakenDecrypt +
        " milidetik."
    );
    $("#decryptionOperation").html(
      "<span class='fw-bold'>Operasi Enkripsi: </span>" +
        encryptedMessage.length +
        " karakter, " +
        result.operationCountDecrypt +
        " operasi."
    );
  });
});
