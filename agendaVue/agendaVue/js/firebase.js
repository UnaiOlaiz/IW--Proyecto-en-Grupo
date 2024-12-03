import { initializeApp } from 'https://www.gstatic.com/firebasejs/9.17.1/firebase-app.js';
import { getFirestore } from 'https://www.gstatic.com/firebasejs/9.17.1/firebase-firestore.js';




const firebaseConfig = {
  apiKey: "AIzaSyAG28ZgepxiX5SyCCkUcXnFPSJfswCAeg4",
  authDomain: "agenda-vue-28393.firebaseapp.com",
  projectId: "agenda-vue-28393",
  storageBucket: "agenda-vue-28393.firebasestorage.app",
  messagingSenderId: "691035398644",
  appId: "1:691035398644:web:df650d0090d60fd88cd9a1",
  measurementId: "G-G990N8WGMQ"
};

const firebaseApp = initializeApp(firebaseConfig);

const db = getFirestore(firebaseApp);

export { db, firebaseApp };
