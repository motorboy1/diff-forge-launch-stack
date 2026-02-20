# APPLY — ops__retry__controlled_backoff_loop__v1.0

## Prerequisites
- Rails 7+ or any Ruby application
- Logger configured

## Apply Steps

1. **Apply the patch:**
   ```bash
   git apply changes.patch
   ```

2. **Use in your code:**
   ```ruby
   backoff = ControlledBackoff.new(
     max_retries: 5,
     base_delay: 1.0,
     circuit_threshold: 5,
     retryable_exceptions: [Net::OpenTimeout, Faraday::TimeoutError]
   )

   result = backoff.execute do
     ExternalApi.fetch_data(params)
   end
   ```

## Verification

1. Test with a failing external call — should retry with increasing delays
2. After 5 consecutive failures — circuit should open, subsequent calls raise `CircuitOpenError`
3. Wait 30s — circuit should enter half-open state and allow one test call

## Rollback

Remove usage from calling code. Delete `lib/controlled_backoff.rb`.
