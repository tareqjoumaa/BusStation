/* ====================================================
   BUS STATION ADMIN — dashboard.js
   ==================================================== */

'use strict';

// ── Live Clock ──────────────────────────────────────
function updateClock() {
  const el = document.getElementById('topbarTime');
  if (!el) return;
  const now = new Date();
  el.textContent = now.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', hour12: false });
}
setInterval(updateClock, 1000);
updateClock();

// ── Animated Counters ───────────────────────────────
function animateCounter(el) {
  const target = parseInt(el.dataset.target, 10);
  const prefix = el.dataset.prefix || '';
  const suffix = el.dataset.suffix || '';
  const duration = 1800;
  const steps = 60;
  const increment = target / steps;
  let current = 0;
  let step = 0;

  const ease = (t) => t < 0.5 ? 4*t*t*t : 1 - Math.pow(-2*t + 2, 3) / 2;

  function tick() {
    step++;
    const progress = ease(step / steps);
    current = Math.round(progress * target);
    el.textContent = prefix + current.toLocaleString() + suffix;
    if (step < steps) requestAnimationFrame(tick);
    else el.textContent = prefix + target.toLocaleString() + suffix;
  }
  requestAnimationFrame(tick);
}

// Observe counters using IntersectionObserver
const counterObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting && !entry.target.dataset.counted) {
      entry.target.dataset.counted = 'true';
      animateCounter(entry.target);
    }
  });
}, { threshold: 0.3 });

document.querySelectorAll('.counter').forEach(el => counterObserver.observe(el));

// ── Toast Notifications ─────────────────────────────
function showToast(message, type = 'info', duration = 3500) {
  const icons = { success: 'fas fa-check-circle', error: 'fas fa-times-circle', info: 'fas fa-info-circle', warning: 'fas fa-exclamation-triangle' };
  const container = document.getElementById('toastContainer');
  if (!container) return;

  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  toast.innerHTML = `<i class="${icons[type] || icons.info} toast-icon"></i><span>${message}</span>`;
  container.appendChild(toast);

  setTimeout(() => {
    toast.classList.add('fade-out');
    setTimeout(() => toast.remove(), 350);
  }, duration);
}

// Expose globally
window.showToast = showToast;

// ── Fullscreen Toggle ───────────────────────────────
const fullscreenBtn = document.getElementById('fullscreenBtn');
if (fullscreenBtn) {
  fullscreenBtn.addEventListener('click', () => {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen();
      fullscreenBtn.innerHTML = '<i class="fas fa-compress"></i>';
    } else {
      document.exitFullscreen();
      fullscreenBtn.innerHTML = '<i class="fas fa-expand"></i>';
    }
  });
}

// ── Sidebar Toggle ──────────────────────────────────
const sidebarToggle = document.getElementById('sidebarToggle');
const sidebar = document.getElementById('sidebar');
const mainWrapper = document.getElementById('mainWrapper');

if (sidebarToggle && sidebar) {
  sidebarToggle.addEventListener('click', () => {
    const collapsed = sidebar.style.width === '70px';
    sidebar.style.width = collapsed ? 'var(--sidebar-w)' : '70px';
    if (mainWrapper) {
      mainWrapper.style.marginLeft = collapsed ? 'var(--sidebar-w)' : '70px';
    }
  });
}

// ── Table Row Hover Glow ────────────────────────────
document.querySelectorAll('.data-table tbody tr').forEach(row => {
  row.addEventListener('mouseenter', () => {
    row.style.transition = 'background 0.18s ease, box-shadow 0.18s ease';
  });
});

// ── Search Bar Keyboard Shortcut ────────────────────
document.addEventListener('keydown', (e) => {
  if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
    e.preventDefault();
    const search = document.getElementById('globalSearch') || document.querySelector('.search-bar input');
    if (search) {
      search.focus();
      search.select();
    }
  }
  if (e.key === 'Escape') {
    const modals = document.querySelectorAll('.modal-overlay');
    modals.forEach(m => m.style.display = 'none');
  }
});

// ── Animate Rows on Scroll ──────────────────────────
const rowObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.animationPlayState = 'running';
      rowObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.anim-row').forEach(row => {
  row.style.animationPlayState = 'paused';
  rowObserver.observe(row);
});

// ── Seat Fill Animation ─────────────────────────────
const seatObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const fill = entry.target;
      fill.style.transition = 'width 1s cubic-bezier(0.4,0,0.2,1)';
      seatObserver.unobserve(fill);
    }
  });
}, { threshold: 0.5 });

document.querySelectorAll('.seat-fill, .perf-fill').forEach(el => seatObserver.observe(el));

// ── Global search filter hint ───────────────────────
const globalSearch = document.getElementById('globalSearch');
if (globalSearch) {
  globalSearch.setAttribute('placeholder', 'Search... (Ctrl+K)');
}

// ── Init complete toast ─────────────────────────────
window.addEventListener('DOMContentLoaded', () => {
  setTimeout(() => showToast('Dashboard loaded successfully', 'success', 2500), 600);
});
