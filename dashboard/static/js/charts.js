/* ====================================================
   BUS STATION ADMIN — charts.js
   Chart.js chart definitions for home dashboard
   ==================================================== */

'use strict';

const COLORS = {
  blue:   '#3b82f6',
  green:  '#10b981',
  amber:  '#f59e0b',
  red:    '#ef4444',
  purple: '#8b5cf6',
  cyan:   '#06b6d4',
  grid:   'rgba(255,255,255,0.04)',
  text:   '#9aa4bf',
};

const chartDefaults = {
  responsive: true,
  maintainAspectRatio: false,
  animation: { duration: 1100, easing: 'easeOutQuart' },
  plugins: { legend: { display: false }, tooltip: { backgroundColor: '#131a2e', titleColor: '#e2e8f7', bodyColor: '#9aa4bf', borderColor: '#1d2742', borderWidth: 1, padding: 10, cornerRadius: 8, displayColors: false } },
};

const scaleDefaults = {
  x: { grid: { color: COLORS.grid }, ticks: { color: COLORS.text, font: { size: 11 } } },
  y: { grid: { color: COLORS.grid }, ticks: { color: COLORS.text, font: { size: 11 } } },
};

function buildGradient(ctx, color, alpha = 0.25) {
  const gradient = ctx.createLinearGradient(0, 0, 0, 200);
  gradient.addColorStop(0, color.replace(')', `, ${alpha})`).replace('rgb', 'rgba'));
  gradient.addColorStop(1, color.replace(')', ', 0)').replace('rgb', 'rgba'));
  return gradient;
}

function hexToRgb(hex) {
  const r = parseInt(hex.slice(1,3),16);
  const g = parseInt(hex.slice(3,5),16);
  const b = parseInt(hex.slice(5,7),16);
  return `${r},${g},${b}`;
}

document.addEventListener('DOMContentLoaded', () => {
  const data = window.dashboardData || {};

  // ── Reservations Line Chart ────────────────────────
  const lineEl = document.getElementById('reservationsLineChart');
  if (lineEl) {
    const ctx = lineEl.getContext('2d');
    const confirmed = (data.reservations || []).map(d => d.confirmed || 0);
    const completed = (data.reservations || []).map(d => d.completed || 0);
    const labels    = (data.reservations || []).map(d => d.label || '');

    const grad1 = ctx.createLinearGradient(0, 0, 0, 200);
    grad1.addColorStop(0, `rgba(${hexToRgb(COLORS.blue)},0.3)`);
    grad1.addColorStop(1, `rgba(${hexToRgb(COLORS.blue)},0)`);

    const grad2 = ctx.createLinearGradient(0, 0, 0, 200);
    grad2.addColorStop(0, `rgba(${hexToRgb(COLORS.green)},0.25)`);
    grad2.addColorStop(1, `rgba(${hexToRgb(COLORS.green)},0)`);

    new Chart(ctx, {
      type: 'line',
      data: {
        labels,
        datasets: [
          {
            label: 'Confirmed',
            data: confirmed,
            borderColor: COLORS.blue,
            backgroundColor: grad1,
            borderWidth: 2.5,
            fill: true,
            tension: 0.45,
            pointRadius: 3,
            pointBackgroundColor: COLORS.blue,
            pointBorderWidth: 0,
            pointHoverRadius: 6,
          },
          {
            label: 'Completed',
            data: completed,
            borderColor: COLORS.green,
            backgroundColor: grad2,
            borderWidth: 2.5,
            fill: true,
            tension: 0.45,
            pointRadius: 3,
            pointBackgroundColor: COLORS.green,
            pointBorderWidth: 0,
            pointHoverRadius: 6,
          }
        ]
      },
      options: {
        ...chartDefaults,
        plugins: {
          ...chartDefaults.plugins,
          legend: {
            display: false,
          },
          tooltip: { ...chartDefaults.plugins.tooltip, displayColors: true }
        },
        scales: scaleDefaults,
      }
    });
  }

  // ── Booking Status Donut ──────────────────────────
  const donutEl = document.getElementById('statusDonutChart');
  if (donutEl) {
    const st = data.statuses || {};
    new Chart(donutEl, {
      type: 'doughnut',
      data: {
        labels: ['Confirmed', 'Pending', 'Cancelled', 'Completed'],
        datasets: [{
          data: [st.confirmed || 0, st.pending || 0, st.cancelled || 0, st.completed || 0],
          backgroundColor: [COLORS.green, COLORS.amber, COLORS.red, COLORS.purple],
          borderWidth: 0,
          hoverOffset: 8,
        }]
      },
      options: {
        ...chartDefaults,
        cutout: '72%',
        plugins: {
          ...chartDefaults.plugins,
          legend: {
            display: true,
            position: 'bottom',
            labels: { color: COLORS.text, padding: 10, font: { size: 11 }, boxWidth: 10, borderRadius: 3 }
          }
        },
        animation: { animateRotate: true, duration: 1200 }
      }
    });
  }

  // ── Revenue Bar Chart ─────────────────────────────
  const barEl = document.getElementById('revenueBarChart');
  if (barEl) {
    const rev = data.revenue || [];
    new Chart(barEl, {
      type: 'bar',
      data: {
        labels: rev.map(d => d.label),
        datasets: [{
          label: 'Revenue ($)',
          data: rev.map(d => d.value),
          backgroundColor: `rgba(${hexToRgb(COLORS.blue)},0.3)`,
          borderColor: COLORS.blue,
          borderWidth: 2,
          borderRadius: 6,
          hoverBackgroundColor: `rgba(${hexToRgb(COLORS.blue)},0.5)`,
        }]
      },
      options: {
        ...chartDefaults,
        scales: {
          ...scaleDefaults,
          y: { ...scaleDefaults.y, ticks: { ...scaleDefaults.y.ticks, callback: v => '$' + v.toLocaleString() } }
        },
      }
    });
  }

  // ── Routes Pie Chart ──────────────────────────────
  const pieEl = document.getElementById('routesPieChart');
  if (pieEl) {
    const routes = data.routes || [];
    new Chart(pieEl, {
      type: 'doughnut',
      data: {
        labels: routes.map(r => r.label),
        datasets: [{
          data: routes.map(r => r.value),
          backgroundColor: [COLORS.blue, COLORS.green, COLORS.amber, COLORS.red, COLORS.purple, COLORS.cyan],
          borderWidth: 0,
          hoverOffset: 8,
        }]
      },
      options: {
        ...chartDefaults,
        cutout: '55%',
        plugins: {
          ...chartDefaults.plugins,
          legend: {
            display: true,
            position: 'bottom',
            labels: { color: COLORS.text, padding: 8, font: { size: 10 }, boxWidth: 8 }
          }
        }
      }
    });
  }

  // ── Occupancy Horizontal Bar ──────────────────────
  const occEl = document.getElementById('occupancyChart');
  if (occEl) {
    const occ = data.occupancy || [];
    new Chart(occEl, {
      type: 'bar',
      data: {
        labels: occ.map(o => o.label),
        datasets: [{
          label: 'Occupancy %',
          data: occ.map(o => o.value),
          backgroundColor: occ.map(o =>
            o.value >= 80 ? `rgba(${hexToRgb(COLORS.green)},0.4)` :
            o.value >= 60 ? `rgba(${hexToRgb(COLORS.blue)},0.4)` :
            `rgba(${hexToRgb(COLORS.amber)},0.4)`
          ),
          borderColor: occ.map(o =>
            o.value >= 80 ? COLORS.green :
            o.value >= 60 ? COLORS.blue  : COLORS.amber
          ),
          borderWidth: 2,
          borderRadius: 4,
        }]
      },
      options: {
        ...chartDefaults,
        indexAxis: 'y',
        scales: {
          x: { ...scaleDefaults.x, max: 100, ticks: { ...scaleDefaults.x.ticks, callback: v => v + '%' } },
          y: scaleDefaults.y,
        }
      }
    });
  }
});
