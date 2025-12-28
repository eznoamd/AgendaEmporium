-- =====================================================
-- BANCO DE DADOS: agenda_clinica (SQLite)
-- =====================================================

PRAGMA foreign_keys = ON;

-- =====================================================
-- STATUS (cores / estados do agendamento)
-- =====================================================
CREATE TABLE IF NOT EXISTS statuses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    color_hex TEXT NOT NULL,
    active INTEGER DEFAULT 1
);

-- =====================================================
-- TIPOS DE SERVIÇO (antigo "tipo")
-- =====================================================
CREATE TABLE IF NOT EXISTS service_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    duration INTEGER,
    filters TEXT,
    active INTEGER DEFAULT 1
);

-- =====================================================
-- TÉCNICOS (antiga "tecnica")
-- =====================================================
CREATE TABLE IF NOT EXISTS technicians (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    active INTEGER DEFAULT 1
);

-- =====================================================
-- CLIENTES
-- =====================================================
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    code TEXT,
    active INTEGER DEFAULT 1
);

-- =====================================================
-- AGENDAMENTOS (TABELA CENTRAL)
-- =====================================================
CREATE TABLE IF NOT EXISTS appointments (
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
CREATE INDEX IF NOT EXISTS idx_appointments_date
ON appointments(date);

CREATE INDEX IF NOT EXISTS idx_appointments_technician
ON appointments(technician_id);

CREATE INDEX IF NOT EXISTS idx_appointments_client
ON appointments(client_id);


-- =====================================================
-- SEEDS
-- =====================================================
CREATE TABLE IF NOT EXISTS seeds (
    name TEXT NOT NULL,
    version INTEGER NOT NULL,
    applied_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (name, version)
);



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


-- Procedimentos / Tipos padrão
INSERT INTO service_types (name, duration, filters, active) VALUES

('Lipo sem cortes',30,
'lipo liposemcortes lipoaspiracao gordura gordura_localizada',1),

('Carboxiterapia',30,
'carbox carboxiterapia carboxiterapia gordura celulite',1),

('Criolipólise/Crio de placas',120,
'crio criolipolise criopolise criolipo placas congelamento gordura',1),

('Criofrequência',30,
'criofrequencia crio frequencia radiofrequencia flacidez',1),

('Radiofrequência',30,
'radiofrequencia radio frequencia rf flacidez',1),

('Corrente Russa',40,
'corrente russa corrente russa eletro estimulacao',1),

('Endermologia',30,
'endermologia endermo massagem celulite',1),

('Ondas de Choque',NULL,
'ondas choque onda choque impacto',1),

('Drenagem',NULL,
'drenagem drenagemlinfatica dren linfatica massagem',1),

('Descolamento',NULL,
'descolamento soltar tecido massagem profunda',1),

('PEIM',NULL,
'peim vasinhos microvarizes',1),

('Powerpump',NULL,
'powerpump pump musculacao eletro',1),

('Venus freeze',NULL,
'venus freeze venusfreeze radiofrequencia flacidez',1),

('Toxina Botulinica',60,
'botox toxina botulinica botulinum rugas',1),

('Preenchimento',60,
'preenchimento preench facial acido hialuronico',1),

('Limpeza de pele',120,
'limpeza pele limpeza_de_pele facial espinha cravo',1),

('Peeling quimico',NULL,
'peeling quimico peelingquimico acido manchas',1),

('Peeling de diamante',NULL,
'peeling diamante peelingdiamante microdermoabrasao',1),

('Microagulhamento',NULL,
'microagulhamento micro agulhamento microagulha',1),

('Jato de plasma',NULL,
'jato plasma jato_plasma plasmajet',1),

('Skinbooster',NULL,
'skinbooster skin booster hidratacao pele',1),

('Enzima',NULL,
'enzima enzimas lipolitica gordura',1),

('Manta térmica',30,
'manta termica manta_termica calor gordura',1),

-- ULTRASSOM MICROFOCADO
('Ultrassom Microfocado - full face',90,
'ultrassom microfocado full face rosto facial',1),

('Ultrassom Microfocado - terço inferior',90,
'ultrassom microfocado terco inferior rosto',1),

('Ultrassom Microfocado - terço superior',90,
'ultrassom microfocado terco superior testa',1),

('Ultrassom Microfocado - intimo',90,
'ultrassom microfocado intimo vaginal',1),

('Ultrassom Microfocado - pescoço',90,
'ultrassom microfocado pescoco pescoco',1),

('Ultrassom Microfocado - papada',90,
'ultrassom microfocado papada queixo',1),

('Ultrassom Microfocado - gluteo',90,
'ultrassom microfocado gluteo bumbum',1),

('Ultrassom Microfocado - infra gluteo',90,
'ultrassom microfocado infra gluteo embaixo bumbum',1),

('Ultrassom Microfocado - colo',90,
'ultrassom microfocado colo peito',1),

('Ultrassom Microfocado - abdomen superior',90,
'ultrassom microfocado abdomen superior barriga',1),

('Ultrassom Microfocado - abdomen inferior',90,
'ultrassom microfocado abdomen inferior barriga',1),

('Ultrassom Microfocado - culote',90,
'ultrassom microfocado culote lateral coxa',1),

('Ultrassom Microfocado - braço posterior',90,
'ultrassom microfocado braco posterior triceps',1),

('Ultrassom Microfocado - joelho',90,
'ultrassom microfocado joelho',1),

('Ultrassom Microfocado - flancos',90,
'ultrassom microfocado flancos lateral barriga',1),

('Ultrassom Microfocado - posterior de coxa',90,
'ultrassom microfocado posterior coxa atras',1),

('Ultrassom Microfocado - mãos',90,
'ultrassom microfocado maos mao',1),

('Ultrassom Microfocado - grandes labios',90,
'ultrassom microfocado grandes labios genital',1),

('Ultrassom Microfocado - pre axilar',90,
'ultrassom microfocado pre axilar lateral axila',1),

('Ultrassom Microfocado - escapula',90,
'ultrassom microfocado escapula costas',1),

('Ultrassom Microfocado - interno de coxa',90,
'ultrassom microfocado interno coxa dentro',1),

-- LASER
('Laser - abdomên',30,
'laser abdomen barriga depilacao',1),

('Laser - Ante braços',30,
'laser antebraco ante braco depilacao',1),

('Laser - Aréolas + seio',30,
'laser areola seio mama',1),

('Laser - Axilas',30,
'laser axila axilas depilacao',1),

('Laser - barba masculina',30,
'laser barba masculino rosto',1),

('Laser - Braço completo',30,
'laser braco completo depilacao',1),

('Laser - buço',30,
'laser buco bigode',1),

('Laser - costas',30,
'laser costas dorso',1),

('Laser - coxa completa',30,
'laser coxa completa perna',1),

('Laser - facial completo',30,
'laser facial rosto completo',1),

('Laser - faixa da barba',30,
'laser faixa barba',1),

('Laser - glabela',5,
'laser glabela entre sobrancelha',1),

('Laser - gluteos',30,
'laser gluteos bumbum',1),

('Laser - joelho',30,
'laser joelho',1),

('Laser - lateral do rosto',30,
'laser lateral rosto',1),

('Laser - linha alba',30,
'laser linha alba barriga',1),

('Laser - lombar',30,
'laser lombar costas',1),

('Laser - mãos',30,
'laser maos mao',1),

('Laser - maxilar',30,
'laser maxilar mandibula',1),

('Laser - meia perna',30,
'laser meia perna canela',1),

('Laser - meio braço',30,
'laser meio braco',1),

('Laser - mento',30,
'laser mento queixo',1),

('Laser - nuca',30,
'laser nuca pescoco',1),

('Laser - ombros',30,
'laser ombros',1),

('Laser - peito',30,
'laser peito torax',1),

('Laser - perianal',30,
'laser perianal anal',1),

('Laser - pernas inteiras',30,
'laser pernas inteiras perna completa',1),

('Laser - pés',30,
'laser pes pe',1),

('Laser - testa',30,
'laser testa fronte',1),

('Laser - virilha',30,
'laser virilha bikini',1);
