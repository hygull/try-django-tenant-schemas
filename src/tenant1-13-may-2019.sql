--
-- PostgreSQL database dump
--

-- Dumped from database version 11.2
-- Dumped by pg_dump version 11.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: tenant1; Type: SCHEMA; Schema: -; Owner: hygull
--

CREATE SCHEMA tenant1;


ALTER SCHEMA tenant1 OWNER TO hygull;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: books_author; Type: TABLE; Schema: tenant1; Owner: hygull
--

CREATE TABLE tenant1.books_author (
    id integer NOT NULL,
    name character varying(50)
);


ALTER TABLE tenant1.books_author OWNER TO hygull;

--
-- Name: books_author_id_seq; Type: SEQUENCE; Schema: tenant1; Owner: hygull
--

CREATE SEQUENCE tenant1.books_author_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE tenant1.books_author_id_seq OWNER TO hygull;

--
-- Name: books_author_id_seq; Type: SEQUENCE OWNED BY; Schema: tenant1; Owner: hygull
--

ALTER SEQUENCE tenant1.books_author_id_seq OWNED BY tenant1.books_author.id;


--
-- Name: books_book; Type: TABLE; Schema: tenant1; Owner: hygull
--

CREATE TABLE tenant1.books_book (
    id integer NOT NULL,
    name character varying(50),
    price double precision NOT NULL,
    author_id integer NOT NULL
);


ALTER TABLE tenant1.books_book OWNER TO hygull;

--
-- Name: books_book_id_seq; Type: SEQUENCE; Schema: tenant1; Owner: hygull
--

CREATE SEQUENCE tenant1.books_book_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE tenant1.books_book_id_seq OWNER TO hygull;

--
-- Name: books_book_id_seq; Type: SEQUENCE OWNED BY; Schema: tenant1; Owner: hygull
--

ALTER SEQUENCE tenant1.books_book_id_seq OWNED BY tenant1.books_book.id;


--
-- Name: books_pincode; Type: TABLE; Schema: tenant1; Owner: hygull
--

CREATE TABLE tenant1.books_pincode (
    id integer NOT NULL,
    officename character varying(255),
    pincode character varying(255),
    officetype character varying(255),
    deliverystatus character varying(255),
    divisionname character varying(255),
    regionname character varying(255),
    circlename character varying(255),
    taluk character varying(255),
    districtname character varying(255),
    statename character varying(255)
);


ALTER TABLE tenant1.books_pincode OWNER TO hygull;

--
-- Name: books_pincode_id_seq; Type: SEQUENCE; Schema: tenant1; Owner: hygull
--

CREATE SEQUENCE tenant1.books_pincode_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE tenant1.books_pincode_id_seq OWNER TO hygull;

--
-- Name: books_pincode_id_seq; Type: SEQUENCE OWNED BY; Schema: tenant1; Owner: hygull
--

ALTER SEQUENCE tenant1.books_pincode_id_seq OWNED BY tenant1.books_pincode.id;


--
-- Name: django_content_type; Type: TABLE; Schema: tenant1; Owner: hygull
--

CREATE TABLE tenant1.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE tenant1.django_content_type OWNER TO hygull;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: tenant1; Owner: hygull
--

CREATE SEQUENCE tenant1.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE tenant1.django_content_type_id_seq OWNER TO hygull;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: tenant1; Owner: hygull
--

ALTER SEQUENCE tenant1.django_content_type_id_seq OWNED BY tenant1.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: tenant1; Owner: hygull
--

CREATE TABLE tenant1.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE tenant1.django_migrations OWNER TO hygull;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: tenant1; Owner: hygull
--

CREATE SEQUENCE tenant1.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE tenant1.django_migrations_id_seq OWNER TO hygull;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: tenant1; Owner: hygull
--

ALTER SEQUENCE tenant1.django_migrations_id_seq OWNED BY tenant1.django_migrations.id;


--
-- Name: users_user; Type: TABLE; Schema: tenant1; Owner: hygull
--

CREATE TABLE tenant1.users_user (
    id integer NOT NULL,
    name character varying(50),
    username character varying(10)
);


ALTER TABLE tenant1.users_user OWNER TO hygull;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: tenant1; Owner: hygull
--

CREATE SEQUENCE tenant1.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE tenant1.users_user_id_seq OWNER TO hygull;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: tenant1; Owner: hygull
--

ALTER SEQUENCE tenant1.users_user_id_seq OWNED BY tenant1.users_user.id;


--
-- Name: books_author id; Type: DEFAULT; Schema: tenant1; Owner: hygull
--

ALTER TABLE ONLY tenant1.books_author ALTER COLUMN id SET DEFAULT nextval('tenant1.books_author_id_seq'::regclass);


--
-- Name: books_book id; Type: DEFAULT; Schema: tenant1; Owner: hygull
--

ALTER TABLE ONLY tenant1.books_book ALTER COLUMN id SET DEFAULT nextval('tenant1.books_book_id_seq'::regclass);


--
-- Name: books_pincode id; Type: DEFAULT; Schema: tenant1; Owner: hygull
--

ALTER TABLE ONLY tenant1.books_pincode ALTER COLUMN id SET DEFAULT nextval('tenant1.books_pincode_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: tenant1; Owner: hygull
--

ALTER TABLE ONLY tenant1.django_content_type ALTER COLUMN id SET DEFAULT nextval('tenant1.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: tenant1; Owner: hygull
--

ALTER TABLE ONLY tenant1.django_migrations ALTER COLUMN id SET DEFAULT nextval('tenant1.django_migrations_id_seq'::regclass);


--
-- Name: users_user id; Type: DEFAULT; Schema: tenant1; Owner: hygull
--

ALTER TABLE ONLY tenant1.users_user ALTER COLUMN id SET DEFAULT nextval('tenant1.users_user_id_seq'::regclass);


--
-- Data for Name: books_author; Type: TABLE DATA; Schema: tenant1; Owner: hygull
--

COPY tenant1.books_author (id, name) FROM stdin;
\.


--
-- Data for Name: books_book; Type: TABLE DATA; Schema: tenant1; Owner: hygull
--

COPY tenant1.books_book (id, name, price, author_id) FROM stdin;
\.


--
-- Data for Name: books_pincode; Type: TABLE DATA; Schema: tenant1; Owner: hygull
--

COPY tenant1.books_pincode (id, officename, pincode, officetype, deliverystatus, divisionname, regionname, circlename, taluk, districtname, statename) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: tenant1; Owner: hygull
--

COPY tenant1.django_content_type (id, app_label, model) FROM stdin;
1	customers	client
2	customers	credential
3	contenttypes	contenttype
4	auth	permission
5	auth	group
6	auth	user
7	sessions	session
8	sites	site
9	admin	logentry
10	users	user
11	books	author
12	books	pincode
13	books	book
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: tenant1; Owner: hygull
--

COPY tenant1.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2019-05-09 11:03:27.766682+05:30
2	auth	0001_initial	2019-05-09 11:03:27.790513+05:30
3	admin	0001_initial	2019-05-09 11:03:27.803885+05:30
4	admin	0002_logentry_remove_auto_add	2019-05-09 11:03:27.817914+05:30
5	admin	0003_logentry_add_action_flag_choices	2019-05-09 11:03:27.832161+05:30
6	contenttypes	0002_remove_content_type_name	2019-05-09 11:03:27.861642+05:30
7	auth	0002_alter_permission_name_max_length	2019-05-09 11:03:27.870557+05:30
8	auth	0003_alter_user_email_max_length	2019-05-09 11:03:27.887408+05:30
9	auth	0004_alter_user_username_opts	2019-05-09 11:03:27.900271+05:30
10	auth	0005_alter_user_last_login_null	2019-05-09 11:03:27.913559+05:30
11	auth	0006_require_contenttypes_0002	2019-05-09 11:03:27.918292+05:30
12	auth	0007_alter_validators_add_error_messages	2019-05-09 11:03:27.933066+05:30
13	auth	0008_alter_user_username_max_length	2019-05-09 11:03:27.946333+05:30
14	auth	0009_alter_user_last_name_max_length	2019-05-09 11:03:27.959419+05:30
15	auth	0010_alter_group_name_max_length	2019-05-09 11:03:27.976627+05:30
16	auth	0011_update_proxy_permissions	2019-05-09 11:03:27.984141+05:30
17	books	0001_initial	2019-05-09 11:03:28.016583+05:30
18	customers	0001_initial	2019-05-09 11:03:28.032522+05:30
19	customers	0002_credential	2019-05-09 11:03:28.04016+05:30
20	sessions	0001_initial	2019-05-09 11:03:28.047488+05:30
21	sites	0001_initial	2019-05-09 11:03:28.054373+05:30
22	sites	0002_alter_domain_unique	2019-05-09 11:03:28.061713+05:30
23	users	0001_initial	2019-05-09 11:03:28.073865+05:30
\.


--
-- Data for Name: users_user; Type: TABLE DATA; Schema: tenant1; Owner: hygull
--

COPY tenant1.users_user (id, name, username) FROM stdin;
1	User1	User1Ten1
2	User2-T1	User2T1
3	User3	User3Ten1
4	User4	User4Ten1
\.


--
-- Name: books_author_id_seq; Type: SEQUENCE SET; Schema: tenant1; Owner: hygull
--

SELECT pg_catalog.setval('tenant1.books_author_id_seq', 1, false);


--
-- Name: books_book_id_seq; Type: SEQUENCE SET; Schema: tenant1; Owner: hygull
--

SELECT pg_catalog.setval('tenant1.books_book_id_seq', 1, false);


--
-- Name: books_pincode_id_seq; Type: SEQUENCE SET; Schema: tenant1; Owner: hygull
--

SELECT pg_catalog.setval('tenant1.books_pincode_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: tenant1; Owner: hygull
--

SELECT pg_catalog.setval('tenant1.django_content_type_id_seq', 13, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: tenant1; Owner: hygull
--

SELECT pg_catalog.setval('tenant1.django_migrations_id_seq', 23, true);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: tenant1; Owner: hygull
--

SELECT pg_catalog.setval('tenant1.users_user_id_seq', 4, true);


--
-- Name: books_author books_author_pkey; Type: CONSTRAINT; Schema: tenant1; Owner: hygull
--

ALTER TABLE ONLY tenant1.books_author
    ADD CONSTRAINT books_author_pkey PRIMARY KEY (id);


--
-- Name: books_book books_book_pkey; Type: CONSTRAINT; Schema: tenant1; Owner: hygull
--

ALTER TABLE ONLY tenant1.books_book
    ADD CONSTRAINT books_book_pkey PRIMARY KEY (id);


--
-- Name: books_pincode books_pincode_pkey; Type: CONSTRAINT; Schema: tenant1; Owner: hygull
--

ALTER TABLE ONLY tenant1.books_pincode
    ADD CONSTRAINT books_pincode_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: tenant1; Owner: hygull
--

ALTER TABLE ONLY tenant1.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: tenant1; Owner: hygull
--

ALTER TABLE ONLY tenant1.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: tenant1; Owner: hygull
--

ALTER TABLE ONLY tenant1.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: users_user users_user_pkey; Type: CONSTRAINT; Schema: tenant1; Owner: hygull
--

ALTER TABLE ONLY tenant1.users_user
    ADD CONSTRAINT users_user_pkey PRIMARY KEY (id);


--
-- Name: books_book_author_id_8b91747b; Type: INDEX; Schema: tenant1; Owner: hygull
--

CREATE INDEX books_book_author_id_8b91747b ON tenant1.books_book USING btree (author_id);


--
-- Name: books_book books_book_author_id_8b91747b_fk_books_author_id; Type: FK CONSTRAINT; Schema: tenant1; Owner: hygull
--

ALTER TABLE ONLY tenant1.books_book
    ADD CONSTRAINT books_book_author_id_8b91747b_fk_books_author_id FOREIGN KEY (author_id) REFERENCES tenant1.books_author(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

