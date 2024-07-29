const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
const cors = require('cors');

const app = express();
app.use(cors()); // Mengaktifkan CORS
app.use(express.json()); // Middleware untuk parse JSON request body

// Buat router
const router = express.Router();

// Proxy untuk Inquiry Transaction
router.post('/api', createProxyMiddleware({
    target: 'https://sandbox-api.espay.id',
    changeOrigin: true,
    pathRewrite: {
        '^/api': '/rest/biller/inquirytransaction',
    },
    onProxyReq: (proxyReq, req, res) => {
        // Menambahkan header jika diperlukan
        proxyReq.setHeader('Access-Control-Allow-Origin', '*');
    },
    onError: (err, req, res) => {
        console.error(err);
        res.status(500).send('Something went wrong with the proxy.');
    }
}));

// Proxy untuk Payment Report
router.post('/api/payment', createProxyMiddleware({
    target: 'https://sandbox-api.espay.id',
    changeOrigin: true,
    pathRewrite: {
        '^/api/payment': '/rest/biller/paymentreport',
    },
    onProxyReq: (proxyReq, req, res) => {
        // Menambahkan header jika diperlukan
        proxyReq.setHeader('Access-Control-Allow-Origin', '*');
    },
    onError: (err, req, res) => {
        console.error(err);
        res.status(500).send('Something went wrong with the proxy.');
    }
}));

// Gunakan router di aplikasi
app.use('/data', router);

// Jalankan server
app.listen(3000, () => {
    console.log('Proxy server is running on http://localhost:3000');
});
