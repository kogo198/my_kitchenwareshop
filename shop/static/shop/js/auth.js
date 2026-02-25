/* ============================================================
   MY KITCHENWARE SHOP – Auth JS
   ============================================================ */
document.addEventListener('DOMContentLoaded', () => {

    /* --- Password visibility toggle --- */
    document.querySelectorAll('.input-toggle').forEach(btn => {
        btn.addEventListener('click', () => {
            const input = btn.previousElementSibling;
            if (!input) return;
            if (input.type === 'password') {
                input.type = 'text';
                btn.textContent = '🙈';
            } else {
                input.type = 'password';
                btn.textContent = '👁';
            }
        });
    });

    /* --- Password strength meter --- */
    const pwInput = document.getElementById('id_password1') || document.getElementById('id_password');
    const fillBar = document.getElementById('strengthFill');
    const strengthTxt = document.getElementById('strengthText');

    if (pwInput && fillBar) {
        pwInput.addEventListener('input', () => {
            const val = pwInput.value;
            let score = 0;
            if (val.length >= 8) score++;
            if (/[A-Z]/.test(val)) score++;
            if (/[0-9]/.test(val)) score++;
            if (/[^A-Za-z0-9]/.test(val)) score++;

            const levels = [
                { width: '0%', color: 'transparent', text: '' },
                { width: '25%', color: '#e05252', text: 'Weak' },
                { width: '50%', color: '#e8a045', text: 'Fair' },
                { width: '75%', color: '#4caf76', text: 'Good' },
                { width: '100%', color: '#2ecc71', text: 'Strong 💪' },
            ];

            const lvl = val.length === 0 ? levels[0] : levels[Math.min(score, 4)];
            fillBar.style.width = lvl.width;
            fillBar.style.background = lvl.color;
            if (strengthTxt) strengthTxt.textContent = lvl.text;
        });
    }

    /* --- Client-side form validation --- */
    const signupForm = document.getElementById('signupForm');
    if (signupForm) {
        signupForm.addEventListener('submit', e => {
            const pw1 = document.getElementById('id_password1');
            const pw2 = document.getElementById('id_password2');
            if (pw1 && pw2 && pw1.value !== pw2.value) {
                e.preventDefault();
                const err = document.getElementById('formError');
                if (err) {
                    err.textContent = 'Passwords do not match.';
                    err.style.display = 'flex';
                }
            }
        });
    }

    /* --- Auto-dismiss alerts --- */
    setTimeout(() => {
        document.querySelectorAll('.alert').forEach(el => {
            el.style.transition = 'opacity 0.5s';
            el.style.opacity = '0';
            setTimeout(() => el.remove(), 500);
        });
    }, 5000);
});
