var express = require('express');
var path = require('path');
var port = 3000;
var { engine } = require('express-handlebars');
var app = express();

var VISITOR_SERVER_URL = 'http://3.34.47.148:8000';
var ADMIN_SERVER_URL = 'http://3.34.47.148:8010';

app.use(express.static(path.join(__dirname, 'views')));

// 뷰 디렉토리 설정
app.set('views', path.join(__dirname, 'views', 'templates'));

// 추가로 views/static 경로를 정적 경로로 설정
app.use(express.static(path.join(__dirname, 'views', 'static')));

// Handlebars 엔진 설정
app.engine('handlebars', engine({
  extname: '.handlebars',
  partialsDir: path.join(__dirname, 'views', 'templates', 'include')  // 파셜 폴더 지정
}));
app.set('view engine', 'handlebars');

// request body 설정
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.render('index', {  // index.handlebars
    layout: false  // 레이아웃을 사용하지 않도록 설정
  });
});

app.get('/apply', (req, res) => {
  res.render('apply/apply', {  // apply.handlebars
    layout: false,  // 기본 레이아웃을 사용하지 않도록 설정
    visitorServerUrl: VISITOR_SERVER_URL // Handlebars 템플릿에 전달
  });
});

app.get('/apply/applyok', (req, res) => {
  res.render('apply/applyok', {  // applyok.handlebars
    layout: false  // 기본 레이아웃을 사용하지 않도록 설정
  });
});

app.get('/check', (req, res) => {
  res.render('check/check', {  // check.handlebars
    layout: false  // 기본 레이아웃을 사용하지 않도록 설정
  });
});

app.post('/check/checkok', (req, res) => {
  res.render('check/checkok', {  // checkok.handlebars
    layout: false,  // 기본 레이아웃을 사용하지 않도록 설정
    data: req.body, // POST 요청의 본문에서 파싱된 데이터를 'data' 객체로 뷰에 전달
    visitorServerUrl: VISITOR_SERVER_URL // Handlebars 템플릿에 전달
  });
});

app.get('/intro', (req, res) => {
  res.render('intro/intro', {  // intro.handlebars
    layout: false  // 기본 레이아웃을 사용하지 않도록 설정
  });
});

app.get('/svc', (req, res) => {
  res.render('svc/svc', {  // svc.handlebars
    layout: false  // 기본 레이아웃을 사용하지 않도록 설정
  });
});

app.get('/admin', (req, res) => {
  res.render('admin/admin', {  // admin.handlebars
    layout: false,  // 기본 레이아웃을 사용하지 않도록 설정
    adminServerUrl: ADMIN_SERVER_URL // Handlebars 템플릿에 전달
  });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
