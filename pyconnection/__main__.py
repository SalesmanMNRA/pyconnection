"""
PYConnection - Command line entry point.

Allows quick HTTP requests and Soroush Plus operations from the command line.
"""

import sys
import argparse
from pyconnection import PYConnectionClient, http_get, http_post


def main() -> None:
    parser = argparse.ArgumentParser(
        description="PYConnection SDK - Combined Soroush Plus and HTTP client"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # HTTP GET command
    get_parser = subparsers.add_parser("get", help="Send HTTP GET request")
    get_parser.add_argument("url", help="URL to request")
    get_parser.add_argument("--params", help="JSON-encoded query parameters")
    get_parser.add_argument("--headers", help="JSON-encoded headers")
    get_parser.add_argument("--timeout", type=float, default=30, help="Timeout in seconds")

    # HTTP POST command
    post_parser = subparsers.add_parser("post", help="Send HTTP POST request")
    post_parser.add_argument("url", help="URL to request")
    post_parser.add_argument("--data", help="JSON-encoded form data")
    post_parser.add_argument("--json", help="JSON-encoded JSON body")
    post_parser.add_argument("--headers", help="JSON-encoded headers")
    post_parser.add_argument("--timeout", type=float, default=30, help="Timeout in seconds")

    # Soroush Plus command
    plus_parser = subparsers.add_parser("plus", help="Soroush Plus operations")
    plus_parser.add_argument(
        "--api-id", type=int, required=True, help="Soroush Plus API ID"
    )
    plus_parser.add_argument("--api-hash", required=True, help="Soroush Plus API hash")
    plus_parser.add_argument("--phone", required=True, help="Phone number")
    plus_parser.add_argument(
        "--action", required=True, choices=["send_message", "get_me"]
    )
    plus_parser.add_argument("--username", help="Target username (for send_message)")
    plus_parser.add_argument("--message", help="Message to send")

    args = parser.parse_args()

    if args.command == "get":
        import json

        params = None
        if args.params:
            params = json.loads(args.params)

        headers = None
        if args.headers:
            headers = json.loads(args.headers)

        response = http_get(
            args.url, params=params, headers=headers, timeout=args.timeout
        )
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text[:500]}...")

    elif args.command == "post":
        import json

        data = None
        if args.data:
            data = json.loads(args.data)

        json_body = None
        if args.json:
            json_body = json.loads(args.json)

        headers = None
        if args.headers:
            headers = json.loads(args.headers)

        response = http_post(
            args.url,
            data=data,
            json=json_body,
            headers=headers,
            timeout=args.timeout,
        )
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text[:500]}...")

    elif args.command == "plus":
        import asyncio

        from pyconnection import PYConnectionClient

        async def run():
            client = PYConnectionClient(
                api_id=args.api_id,
                api_hash=args.api_hash,
                phone_number=args.phone,
            )

            if args.action == "send_message":
                if not args.username or not args.message:
                    print("Error: --username and --message required for send_message")
                    sys.exit(1)
                result = await client.send_message(args.username, args.message)
                print(f"Sent message to {args.username}: {result}")
            elif args.action == "get_me":
                result = await client.get_me()
                print(f"User info: {result}")

        asyncio.run(run())

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()