-- by_name
CREATE INDEX idx_name_first
 ON names (LEFT(name, 1));
