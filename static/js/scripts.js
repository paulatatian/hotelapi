// ------------------ HABITACIONES ------------------
async function listarHabitaciones() {
    const res = await fetch('/api/habitaciones/');
    const data = await res.json();
    const list = document.getElementById('habitaciones-list');

    if (list) {
        list.innerHTML = '';
        data.forEach(h => {
            const li = document.createElement('li');
            li.textContent = `ID: ${h.id} | ${h.numero} | ${h.tipo} | $${h.precio}`;
            list.appendChild(li);
        });
    }
}

const formHab = document.getElementById('habitaciones-form');
if (formHab) {
    formHab.addEventListener('submit', async e => {
        e.preventDefault();
        const numero = document.getElementById('numero').value;
        const tipo = document.getElementById('tipo').value;
        const precio = parseInt(document.getElementById('precio').value);

        await fetch('/api/habitaciones/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ numero, tipo, precio })
        });

        listarHabitaciones();
        formHab.reset();
    });
}

listarHabitaciones();


// ------------------ HUESPEDES ------------------
async function listarHuespedes() {
    const res = await fetch('/api/huespedes/');
    const data = await res.json();
    const list = document.getElementById('huespedes-list');

    if (list) {
        list.innerHTML = '';
        data.forEach(h => {
            const li = document.createElement('li');
            li.textContent = `ID: ${h.id} | ${h.nombre} | ${h.email} | ${h.telefono}`;
            list.appendChild(li);
        });
    }
}

const formHues = document.getElementById('huespedes-form');
if (formHues) {
    formHues.addEventListener('submit', async e => {
        e.preventDefault();
        const nombre = document.getElementById('nombre').value;
        const email = document.getElementById('email').value;
        const telefono = document.getElementById('telefono').value;

        await fetch('/api/huespedes/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ nombre, email, telefono })
        });

        listarHuespedes();
        formHues.reset();
    });
}

listarHuespedes();


// ------------------ RESERVAS ------------------
async function listarReservas() {
    const res = await fetch('/api/reservas/');
    const data = await res.json();
    const list = document.getElementById('reservas-list');

    if (list) {
        list.innerHTML = '';
        data.forEach(r => {
            const li = document.createElement('li');
            li.textContent = `ID: ${r.id} | Huésped: ${r.huesped_id} | Habitación: ${r.habitacion_id} | Ingreso: ${r.fecha_ingreso} | Salida: ${r.fecha_salida}`;
            list.appendChild(li);
        });
    }
}

const formRes = document.getElementById('reservas-form');
if (formRes) {
    formRes.addEventListener('submit', async e => {
        e.preventDefault();
        const huesped_id = parseInt(document.getElementById('huesped_id').value);
        const habitacion_id = parseInt(document.getElementById('habitacion_id').value);
        const fecha_ingreso = document.getElementById('fecha_ingreso').value;
        const fecha_salida = document.getElementById('fecha_salida').value;

        await fetch('/api/reservas/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ huesped_id, habitacion_id, fecha_ingreso, fecha_salida })
        });

        listarReservas();
        formRes.reset();
    });
}

listarReservas();
