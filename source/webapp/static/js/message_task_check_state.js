function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

async function makeRequest(url, method = 'GET', data = undefined) {
    let opts = {method, headers: {}};

    if (!csrfSafeMethod(method))
        opts.headers['X-CSRFToken'] = getCookie('csrftoken');

    if (data) {
        opts.headers['Content-Type'] = 'application/json';
        opts.body = JSON.stringify(data);
    }

    let response = await fetch(url, opts);

    if (response.ok) {  // нормальный ответ
        return response;
    } else {            // ошибка
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}

let taskUrl = document.getElementById('task_url').href;
let dots = 1;
let progressTitle = document.getElementById('progress-title');
let progressDot = document.getElementById('dot');
let status = document.getElementById('status');
updateProgressTitle();
let timer = setInterval(async function() {
  updateProgressTitle();
  let response = await makeRequest(taskUrl).then((response) => response.json());
  console.log(response)
      let taskStatus = response.task_status
      if (taskStatus === 'SUCCESS') {
        clearTimer('Result:')
        status.innerText = ' ' + response.task_status;

      } else if (taskStatus === 'FAILURE') {
        clearTimer('An error has occurred');
    }
}, 500);

function updateProgressTitle() {
  dots++;
  if (dots > 3) {
    dots = 1;
  }
  progressTitle.innerHTML = 'Progress ';
  progressDot.innerHTML = ' ';
  for (let i = 0; i < dots; i++) {
      progressDot.innerHTML += '.';
  }
}

function clearTimer(message) {
  clearInterval(timer);
  progressTitle.innerHTML = message;
  progressDot.innerHTML = '';
}
