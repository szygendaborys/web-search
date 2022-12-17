--
-- PostgreSQL database dump
--

-- Dumped from database version 13.9 (Debian 13.9-1.pgdg110+1)
-- Dumped by pg_dump version 13.3

-- Started on 2022-12-12 20:25:49

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: airflow
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO airflow;

--
-- TOC entry 3004 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: airflow
--

COMMENT ON SCHEMA public IS 'standard public schema';


--
-- TOC entry 6 (class 2615 OID 17019)
-- Name: search; Type: SCHEMA; Schema: -; Owner: airflow
--

CREATE SCHEMA search;


ALTER SCHEMA search OWNER TO airflow;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 202 (class 1259 OID 17020)
-- Name: search_listings; Type: TABLE; Schema: search; Owner: airflow
--

CREATE TABLE search.search_listings (
    listing_id uuid NOT NULL,
    url character varying NOT NULL,
    title character varying,
    price character varying NOT NULL,
    size character varying NOT NULL,
    deleted_at timestamp without time zone,
    created_at timestamp without time zone DEFAULT now() NOT NULL,
    notification_sent_at timestamp without time zone
);


ALTER TABLE search.search_listings OWNER TO airflow;

--
-- TOC entry 2866 (class 2606 OID 17028)
-- Name: search_listings search_listings_pk; Type: CONSTRAINT; Schema: search; Owner: airflow
--

ALTER TABLE ONLY search.search_listings
    ADD CONSTRAINT search_listings_pk PRIMARY KEY (listing_id);


--
-- TOC entry 2867 (class 1259 OID 17029)
-- Name: search_listings_url_idx; Type: INDEX; Schema: search; Owner: airflow
--

CREATE INDEX search_listings_url_idx ON search.search_listings USING btree (url);


-- Completed on 2022-12-12 20:25:49

--
-- PostgreSQL database dump complete
--

