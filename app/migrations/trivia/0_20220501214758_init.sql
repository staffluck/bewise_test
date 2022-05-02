-- upgrade --
CREATE TABLE IF NOT EXISTS "trivias" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "question_id" INT NOT NULL,
    "question" TEXT NOT NULL,
    "answer" VARCHAR(155) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
