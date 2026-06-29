/* ====================================================
   BUS STATION ADMIN — login.js
   Form validation + submit to Django (which calls API)
   The API call happens server-side in login_view.py
   to avoid CORS issues with busstation.bsite.net
   ==================================================== */

'use strict';

const form       = document.getElementById('loginForm');
const phoneInput = document.getElementById('phoneNumber');
const passInput  = document.getElementById('password');
const submitBtn  = document.getElementById('submitBtn');
const btnLabel   = document.getElementById('btnLabel');
const btnLoading = document.getElementById('btnLoading');
const togglePass = document.getElementById('togglePass');
const toggleIcon = document.getElementById('togglePassIcon');

// ── Password visibility toggle ────────────────────────
togglePass.addEventListener('click', () => {
  const isHidden = passInput.type === 'password';
  passInput.type = isHidden ? 'text' : 'password';
  toggleIcon.className = isHidden ? 'fas fa-eye-slash' : 'fas fa-eye';
});

// ── Real-time validation ──────────────────────────────
phoneInput.addEventListener('blur', () => validatePhone(true));
passInput.addEventListener('blur',  () => validatePass(true));
phoneInput.addEventListener('input', () => {
  if (phoneInput.classList.contains('has-error')) validatePhone(false);
});
passInput.addEventListener('input', () => {
  if (passInput.classList.contains('has-error')) validatePass(false);
});

function validatePhone(showError) {
  const val = phoneInput.value.trim();
  const ok  = val.length >= 7;
  phoneInput.classList.toggle('has-error', !ok && showError);
  phoneInput.classList.toggle('valid', ok);
  document.getElementById('phoneError').textContent = (!ok && showError) ? 'Enter a valid phone number' : '';
  return ok;
}

function validatePass(showError) {
  const val = passInput.value;
  const ok  = val.length >= 6;
  passInput.classList.toggle('has-error', !ok && showError);
  passInput.classList.toggle('valid', ok);
  document.getElementById('passError').textContent = (!ok && showError) ? 'Password must be at least 6 characters' : '';
  return ok;
}

// ── Form submit — just validate then let Django handle it ──
form.addEventListener('submit', (e) => {
  const phoneOk = validatePhone(true);
  const passOk  = validatePass(true);

  if (!phoneOk || !passOk) {
    e.preventDefault();
    return;
  }

  // Show loading spinner while Django processes
  setLoading(true);
  // Let the form submit normally to Django POST
});

function setLoading(loading) {
  submitBtn.disabled = loading;
  btnLabel.style.display   = loading ? 'none' : 'flex';
  btnLoading.style.display = loading ? 'flex' : 'none';
}

// ── Auto-dismiss error banner ─────────────────────────
const banner = document.getElementById('errorBanner');
if (banner) {
  setTimeout(() => {
    banner.style.transition = 'opacity 0.4s ease';
    banner.style.opacity = '0';
    setTimeout(() => banner.style.display = 'none', 400);
  }, 5000);
}

// ── Enter key support ─────────────────────────────────
[phoneInput, passInput].forEach(el => {
  el.addEventListener('keydown', e => {
    if (e.key === 'Enter') form.requestSubmit();
  });
});