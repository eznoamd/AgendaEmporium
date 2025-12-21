-- =====================================================
-- BANCO DE DADOS: agenda_clinica (SQLite)
-- =====================================================

PRAGMA foreign_keys = ON;

-- =====================================================
-- STATUS (cores / estados do agendamento)
-- =====================================================
CREATE TABLE statuses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    color_hex TEXT NOT NULL,
    active INTEGER DEFAULT 1
);

-- =====================================================
-- TIPOS DE SERVIÇO (antigo "tipo")
-- =====================================================
CREATE TABLE service_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    filters TEXT,
    active INTEGER DEFAULT 1
);

-- =====================================================
-- TÉCNICOS (antiga "tecnica")
-- =====================================================
CREATE TABLE technicians (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    active INTEGER DEFAULT 1
);

-- =====================================================
-- CLIENTES
-- =====================================================
CREATE TABLE clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    code TEXT,
    active INTEGER DEFAULT 1
);

-- =====================================================
-- AGENDAMENTOS (TABELA CENTRAL)
-- =====================================================
CREATE TABLE appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    -- Data e horário (ISO 8601)
    date TEXT NOT NULL,          -- YYYY-MM-DD
    start_time TEXT NOT NULL,    -- HH:MM
    end_time TEXT NOT NULL,      -- HH:MM

    -- Relacionamentos
    status_id INTEGER NOT NULL,
    technician_id INTEGER NOT NULL,
    client_id INTEGER,
    service_type_id INTEGER,

    -- Controle
    notes TEXT,
    rescheduled INTEGER DEFAULT 0,
    active INTEGER DEFAULT 1,

    -- Auditoria
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT,

    -- Regras de integridade
    CHECK (start_time < end_time),

    -- ❗ Conflito SOMENTE para o mesmo técnico
    UNIQUE (date, technician_id, start_time),

    FOREIGN KEY (status_id) REFERENCES statuses(id),
    FOREIGN KEY (technician_id) REFERENCES technicians(id),
    FOREIGN KEY (client_id) REFERENCES clients(id),
    FOREIGN KEY (service_type_id) REFERENCES service_types(id)
);

-- =====================================================
-- ÍNDICES (PERFORMANCE)
-- =====================================================
CREATE INDEX idx_appointments_date
ON appointments(date);

CREATE INDEX idx_appointments_technician
ON appointments(technician_id);

CREATE INDEX idx_appointments_client
ON appointments(client_id);

-- =====================================================
-- DADOS INICIAIS (OPCIONAL)
-- =====================================================

-- Status padrão
INSERT INTO statuses (name, color_hex) VALUES
('Disponível', '#E0E0E0'),
('Agendado', '#4CAF50'),
('Cancelado', '#F44336'),
('Reagendado', '#FF9800'),
('Bloqueado', '#9E9E9E');

